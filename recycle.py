import requests
import base64
from PIL import Image

API_KEY = "AIzaSyDn0_wjZYO3ktYXdalT0c4yGrKrhqeXr84"

url = "https://vision.googleapis.com/v1/images:annotate?key="
img_loc = "burger.jpg"
image = base64.b64encode(open(img_loc, "rb").read())

body = {
  "requests":[
    {
      "image":{
        "content": image
      },
      "features":[
        {
          "type":"LABEL_DETECTION"
        }
      ]
    }
  ]
}

r = requests.post(url + API_KEY, json=body)
print(r.content)
