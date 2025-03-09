from bs4 import BeautifulSoup
import requests

# Profile tracker for Github

user_name = input("Enter your username\n")
response = requests.get(f"https://github.com/{user_name}")

soup = BeautifulSoup(response.text, "html.parser")

all_datas = soup.find_all("span", class_="Counter")

repo = all_datas[0].text
stars = all_datas[3].text
print(f"Total Repositories: {repo}")
print(f"Stars: {stars}")
