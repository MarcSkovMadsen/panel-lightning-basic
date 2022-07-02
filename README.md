![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# ⚡ Panel Lightning Basic Web UI

Basic example of a [Panel](https://panel.holoviz.org) [lightning.ai](https://lightning.ai/) Lightning Web UI.

![Panel Lighting Basic Web UI](assets/panel-lightning-basic.gif)

## ⚙️ Install Locally

```bash
git clone https://github.com/MarcSkovMadsen/panel-lightning-basic.git
cd awesome-panel-lightning
```

[Create](https://realpython.com/python-virtual-environments-a-primer/#create-it) and [activate](https://realpython.com/python-virtual-environments-a-primer/#activate-it) your local environment.

Then install the requirements via

```bash
pip install -r requirements.txt
```

Finally you can update the `name` of the app in the [.lightning](.lightning) file.

## Develop Locally

Develop the Panel app locally with hot reload

```bash
panel serve app.py --autoreload --show
```

## 🏃 Run Locally

Run the lightning app locally via

```bash
lightning run app app.py
```

## ☁️ Run in lightning.ai cloud

Run the lightning app in the cloud via

```bash
lightning run app app.py --cloud
```

and follow the instructions
