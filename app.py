import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


cookies = {
}

headers = {
}

params = {
    'detail_source': 'resume_direct',
}

response = requests.get('https://internshala.com/student/resume', params=params, cookies=cookies, headers=headers)


def get_github_username(text):
    # regex = "^(http(s?):\\/\\/)?(www\\.)?github\\.com+\\/([A-Za-z0-9]{1,})+\\/?$"
    soup = BeautifulSoup(text, features="html.parser")
    links = soup.find_all("a")

    github_links = ""

    for link in links:
        git_link_matched = re.findall("https://github.com/([A-Za-z0-9]{1,})+/?$", str(link.get("href")))
        if git_link_matched:
            github_links = git_link_matched

    print(github_links)

    return github_links[0]


def get_github_stats(username):
    stats = dict()
    github_page = urlopen(f"https://github-readme-stats.vercel.app/api?username={username}")
    commit_soup = BeautifulSoup(github_page.read(), features="html.parser")
    texts = commit_soup.find_all("text")

    for text in texts:
        if text.get("data-testid") == "commits":
            stats["commits"] = int(text.get_text())

    print(f'Total commits in (2023): {stats["commits"]}')
    return stats


github_username = get_github_username(response.content)
result = get_github_stats(github_username)
print(result)
