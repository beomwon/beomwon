import feedparser, time

# 팁스선정기사 https://www.venturesquare.net/881567
URL="https://beomcoder.tistory.com/rss" 
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
<div align="center">
  <br><br><br>
  <a href="https://beomcoder.tistory.com">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=B1F767&center=true&vCenter=true&width=435&lines=I'm+Beomwon+Lee%2C;AI+engineer%2C;interested+in+coding." alt="Typing SVG" />
  </a>
  
  <br>
  <p>ᴛʜᴇ ʜᴀʀᴅᴇʀ ʏᴏᴜ ᴡᴏʀᴋ, ᴛʜᴇ ᴍᴏʀᴇ ʟɪᴋᴇʟʏ ʏᴏ ᴄᴀɴ ʀᴇᴀᴄʜ ᴛʜᴇ ɢᴏᴀʟ</p>
  <p align="center">
    <img width="250" height="250" src="https://github.com/beomwon/beomwon/assets/38881094/3c7a0ddd-6f4a-4531-86cf-b535fecff91c">
  </p>
  
  <p align="center"><a href="https://beomcoder.tistory.com/"><img src="https://img.shields.io/badge/blog-A9BCF5?style=flat-square&logo=Undertale&logoColor=white&link=https://beomcoder.tistory.com/"/></a>  <a href="mailto:viva.beom@gmail.com"><img src="https://img.shields.io/badge/mail-D0A9F5?style=flat-square&logo=Gmail&logoColor=white&link=mailto:viva.beom@gmail.com"/></a></p>
  <br>

  <details>
  <summary>𝙍𝙀𝘾𝙀𝙉𝙏 𝘽𝙇𝙊𝙂 𝙋𝙊𝙎𝙏𝙎 🚩</summary>
  <br>
  <div markdown="1">

  |index|date|title|
  |:---:|---|---|
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"|{idx+1}|{time.strftime('%Y/%m/%d', feed_date)}|[{feed['title']}]({feed['link']})|\n"
markdown_text += "</div>\n</details>\n</div>\n"
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
