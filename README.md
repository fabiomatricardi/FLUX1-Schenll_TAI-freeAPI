# FLUX1-Schenll_TAI-freeAPI
How to generate Images with Flux.1-Schnell and free API from Tegether.AI

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/terrarium.png' height=300> <img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/dragon.png' height=300>

Together AI provide free access with API to Top Notch models.

## Flux.1-Schenll is awesome at very small Steps (even only 1 or 4)

Flux.1-Schenll can be used for free (siwth some limitations)
- remotely with an API Key
- on the web with https://api.together.ai/

Free quota:
- 60 Requests Per Minute
- Total 60.000 requests per Months

Register at https://api.together.ai/

---

Remote calls requires the Together package. Recommended to use Python 3.12 to avoid dependency clashes
```
pip install together==1.4.1
```

Or Clone the repo and create a venv and install from requirements
```
python312 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

To run the generation:
```
Python .\GenerateImages.py
```
You will be asked for:
- a valid API key
- a prompt
- a filename, once the miage is genrated


### Some prompt examples
You can find more [here](https://getimg.ai/blog/flux-1-prompt-guide-pro-tips-and-common-mistakes-to-avoid) and [here](https://aimlapi.com/blog/master-the-art-of-ai-top-10-prompts-for-flux-1-by-black-forests-labs)


> A hanging glass terrarium featuring a miniature rainforest scene with colorful orchids and tiny waterfalls. Just beyond the glass, a neon sign reads 'Rainforest Retreat.' The rain-soaked glass creates a beautiful distortion, adding a soft glow to the sign's vibrant colors

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/terrarium.png' height=400> 


---


> Photo realistic scene inspired by LOTR: [A tiny red dragon sleeps curled up in a nest on a medieval wizard's table]. Shot with a macro lens (f/2.8, 50mm) and a Canon EOSR5, the soft focus captures [the cozy morning light filtering through a near by window]. The pastel colors and whimsical steam shapes enhance the serene atmosphere, evoking a DnD RPG setting. The image is rendered in 16K and 8K, highlighting [the intricate details and medieval charm].

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/dragon.png' height=400>

---


> A single tree standing in the middle of the image. The left half of the tree has bright, vibrant red leaves under a bright, sunny blue sky, while the right half has bare branches covered in frost, with a cold, dark, thunderous sky. On the left there's orange, lush grass on the ground; on the right - thick snow. The split is sharp, with the transition happening right down the middle of the tree

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/red-whiteTREE.png' height=400>







