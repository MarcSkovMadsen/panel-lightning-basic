import lightning_app as lapp
import panel as pn
import plotly.express as px

pn.extension("plotly", sizing_mode="stretch_width")

ACCENT = "#792EE5"


def get_panel_theme():
    """Returns 'default' or 'dark'"""
    return pn.state.session_args.get("theme", [b"default"])[0].decode()


def get_plotly_template():
    if get_panel_theme() == "dark":
        return "plotly_dark"
    return "plotly_white"


def get_plot(length=5):
    xseries = [index for index in range(length + 1)]
    yseries = [x**2 for x in xseries]
    fig = px.line(
        x=xseries,
        y=yseries,
        template=get_plotly_template(),
        color_discrete_sequence=[ACCENT],
        range_x=(0, 10),
        markers=True,
    )
    fig.layout.autosize = True
    return fig


def get_view():
    length = pn.widgets.IntSlider(value=5, start=1, end=10, name="Length")
    plot = pn.bind(get_plot, length=length)
    component = pn.Column(length, plot)
    template = pn.template.FastListTemplate(
        title="⚡ Hello Panel + Lightning ⚡", main=[component], accent=ACCENT
    )
    return template


class LitPanel(lapp.LightningWork):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.requests = 0

    def _fast_initial_view(self):
        self.requests += 1
        if self.requests == 1:
            return pn.pane.HTML("<h1>Please refresh the browser to see the app.</h1>")
        else:
            return get_view()

    def run(self):
        pn.serve(
            {"/": self._fast_initial_view},
            port=self.port,
            address=self.host,
            websocket_origin="*",
            show=False,
        )


class LitApp(lapp.LightningFlow):
    def __init__(self):
        super().__init__()
        self.lit_panel = LitPanel(parallel=True)

    def run(self):
        self.lit_panel.run()

    def configure_layout(self):
        tab1 = {"name": "Home", "content": self.lit_panel}
        return tab1

app = lapp.LightningApp(LitApp())

if __name__.startswith("bokeh"):
    LitPanel().view().servable()

    
