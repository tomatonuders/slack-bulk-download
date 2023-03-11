import requests

headers = {"content-type": "application/json; charset=UTF-8",'Authorization':'Bearer {}'.format("<YOUR BEARER TOKEN GOES HERE>")}

d=requests.get("https://slack.com/api/emoji.list", headers=headers).json()
d=d["emoji"]

for item in d.keys():
   image_url = d[item]
   if image_url[0] != "h":
     continue
   print(image_url)
   extension=image_url[-3:]
   img_data = requests.get(image_url).content
   if extension == "gif":
     with open(item+'.gif', 'wb') as handler:
       handler.write(img_data)
   if extension == "png":
     with open(item+'.png','wb') as handler:
       handler.write(img_data)
   if extension == "jpg":
     with open(item+'.jpg', 'wb') as handler:
       handler.write(img_data)
