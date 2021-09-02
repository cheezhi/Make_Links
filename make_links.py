import re
import webbrowser

with open('links.txt', 'r') as f:
    all = f.read()

title = re.findall("title: .+,", all)
for x in range(len(title)):
    title[x]=title[x].split('title: ')[1].split(',')[0]

intro = re.findall("intro: .+,", all)
for x in range(len(intro)):
    intro[x]=intro[x].split('intro: ')[1].split(',')[0]

links = re.findall("link: .+,", all)
for x in range(len(links)):
    links[x]=links[x].split('link: ')[1].split(',')[0]

avatar = re.findall("avatar: .+,", all)
for x in range(len(avatar)):
    avatar[x]=avatar[x].split('avatar: ')[1].split(',')[0]

index_img = re.findall("index_img: .+,", all)
for x in range(len(index_img)):
    index_img[x]=index_img[x].split('index_img: ')[1].split(',')[0]

title_color = re.findall("title_color: .+,", all)
title_color[0]= title_color[0].split('title_color: ')[1].split(',')[0]
title_color = title_color[0]

intro_color = re.findall("intro_color: .+,", all)
intro_color[0]= intro_color[0].split('intro_color: ')[1].split(',')[0]
intro_color = intro_color[0]

bg_img = re.findall("bg_img: .+,", all)
bg_img[0]= bg_img[0].split('bg_img: ')[1].split(',')[0]
bg_img = bg_img[0]

f = open('links.html', 'r+')
f.truncate(0)

f = open('links.html','w')

all_card_code = []

for x in range(len(title)):
    card_code = '<div class="card"><a target="_blank" rel="nofollow" href="{}"><div class="card-img" style="background-image: url({});"></div><div class="card-u"><div class="card-u-a"><img class="card-u-avatar" src="{}"></div><div class="card-u-t"><b class="card-u-t-title">{}</b><p class="card-u-t-text">{}</p></div></div></a></div>'.format(links[x],index_img[x],avatar[x],title[x],intro[x])
    all_card_code.append(card_code)

s2 = ""
seq = (all_card_code)
all_card = s2.join(seq)

html_code = "<!DOCTYPE html><html><head><meta charset='utf-8'><title>links</title><style>* {{margin: 0;padding: 0;}}*::-webkit-scrollbar {{width: 10px;}}*::-webkit-scrollbar-thumb {{border-radius: 5px;background-color: #d4d4d4;}}*::-webkit-scrollbar-thumb :hover {{background-color: #b3b3b3;}}body {{margin: 100px 0;background-position: center;background-image: url('{}');background-size: cover;background-repeat:no-repeat;background-size:100%% 100%; background-attachment: fixed;}}a {{text-decoration: none;}}#card_one {{margin-left: 20%;}}.card {{box-sizing: border-box;margin-top: 20px;margin-right:1vw; margin-left: 3vw;width: 20vw;background: rgba(255, 255, 255, 0.25);box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);backdrop-filter: blur(8.0px);-webkit-backdrop-filter: blur(8.0px);border-radius: 10px;border: 1px solid rgba(255, 255, 255, 0.18);display: inline-block; height: 225px;transition: 0.3s;}}.card:hover {{box-shadow: 0 8px 39px 0 rgba(0, 0, 0, 0.37);transform: translateY(-10px);}}.card-img {{height: 160px;overflow: hidden;border-radius: 10px;margin: 2.5px;background-position: center;background-size: cover;}}.card-u {{padding-top: 10px;height: 45px;position: relative;}}.card-u-a {{width: 50px;position: absolute;left: 0;top: 10px;}}.card-u-avatar {{width: 35px;height: 35px;border-radius: 10px;margin: 5px;}}.card-u-t {{box-sizing: border-box;width: 100%;padding-left: 50px;}}.card-u-t-title {{color: {};line-height: 25px;}}.card-u-t-text {{font-size: 10px;color: {};line-height: 20px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}}@media (max-width: 1000px) {{.card {{width: 40vw !important;}}}}</style></head><body>".format(bg_img, title_color, intro_color)
all_html_code = """
{}
{}
</body>
</html>
""".format(html_code, all_card)


f.write(all_html_code)
f.close()