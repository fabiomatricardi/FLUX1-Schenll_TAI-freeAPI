from together import Together
import requests
from PIL import Image
from io import BytesIO
APIK = input('Your Tegether API Key: ')
prompt = input('/imagine: ')
client = Together(api_key=APIK)
try:
    response = client.images.generate(prompt=prompt,
                    model="black-forest-labs/FLUX.1-schnell-Free", 
                    steps=4, 
                    width=1024, 
                    height=768,
                    n=1)
    imurl = response.data[0].url
    my_res = requests.get(imurl)
    my_img = Image.open(BytesIO(my_res.content))
    my_img.show()
    savename = input('Give me a name (end with .png please): ')
    my_img.save(savename)
except:
    print('Check you API Key is a valid one at https://api.together.ai/settings/api-keys !')
