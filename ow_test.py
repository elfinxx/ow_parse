import requests
from bs4 import BeautifulSoup as bs


def get_competitive_rank_class(url_string):

    if "rank-1.png" in url_string:
        return "Bronze"
    elif "rank-2.png" in url_string:
        return "Silver"
    elif "rank-3.png" in url_string:
        return "Gold"
    elif "rank-4.png" in url_string:
        return "Diamond"
    elif "rank-5.png" in url_string:
        return "Master"
    elif "rank-6.png" in url_string:
        return "Grand Master"
    elif "rank-7.png" in url_string:
        return "GOD"
    else:
        return "ERROR"

ow_url = "https://playoverwatch.com/ko-kr/career/pc/kr/"
sample_bt = "%EB%B0%94%ED%8A%B8-31102"


response = requests.get(ow_url + sample_bt)
body = bs(response.content, 'html.parser')
competitive_rank_value = body.select_one("div.competitive-rank > div")
competitive_rank_img = body.select_one("div.competitive-rank > img")

competitive_most_char = body.select_one("#competitive > section.content-box.max-width-container.hero-comparison-section > div > div.progress-category.is-partial.toggle-display.is-active div > div.bar-text > div.title")
competitive_most_time = body.select_one("#competitive > section.content-box.max-width-container.hero-comparison-section > div > div.progress-category.is-partial.toggle-display.is-active div > div.bar-text > div.description")

print(competitive_rank_value.get_text())
print(get_competitive_rank_class(competitive_rank_img.get('src')))
print(competitive_most_char.get_text())
print(competitive_most_time.get_text())

"#competitive > section.content-box.max-width-container.hero-comparison-section > div > div.progress-category.is-partial.toggle-display.is-active > div:nth-child(1) > div > div.bar-text > div.title"
"#overview-section > div > div.max-width-container.row.content-box.gutter-18 > div > div > div.masthead-player > div > div.competitive-rank > img"
"#overview-section > div > div.max-width-container.row.content-box.gutter-18 > div > div > div.masthead-player > div > div.competitive-rank > div"
"https://playoverwatch.com/ko-kr/search?q=%EB%B0%94%ED%8A%B8-31102"

