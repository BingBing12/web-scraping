from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")
titles = soup.select(".titlelink")

scores = soup.select(".score")
score_list = [int(score.text.split(" ")[0]) for score in scores]
highest_score = max(score_list)
max_index = score_list.index(highest_score)

print(f'Most popular article "{titles[max_index].text}" with {scores[max_index].text} '
      f'\nArticle: {titles[max_index].get("href")}')
