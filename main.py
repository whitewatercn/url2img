import requests
from bs4 import BeautifulSoup
import qrcode
from PIL import Image,ImageDraw,ImageFont
# 输入网址
url = input("请输入网址：")

# 获取网页数据
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 获取标题、图标、和描述
title = soup.title.string
favicon = soup.find('link', rel='icon')
icon_url = favicon['href'] if favicon else None
description = soup.find('meta', {'name': 'description'})
description_content = description['content'] if description else "No Description"


# 生成二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

image = Image.new('RGBA', (800, 600), (255, 255, 255, 255))

# set qrimage
qr_position=(550,350)
qr_image = qr_image.resize((200, 200))
image.paste(qr_image, qr_position)

# set fevicon
icon = Image.open(requests.get(icon_url, stream=True).raw)
icon = icon.resize((200, 200))
icon_position=(550,50)
image.paste(icon, icon_position)

# set font
font = ImageFont.truetype('./Hei.ttf', 24)
title = 'test'
# set title description
draw = ImageDraw.Draw(image)
draw.text((50, 50), title,  fill='red',font=font)

# save output
image.save('test.png')

