import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

from config_local import *
from actions.click_test import *


data = {
    "github": dict()
}


def get_github_username(text):
    # regex = "^(http(s?):\\/\\/)?(www\\.)?github\\.com+\\/([A-Za-z0-9]{1,})+\\/?$"
    soup = BeautifulSoup(text, features="html.parser")
    links = soup.find_all("a")

    github_links = ""

    for link in links:
        exact_link = str(link.get("href"))
        git_link_matched = re.findall("https://github.com/([A-Za-z0-9]{1,})+/?$", exact_link)
        if git_link_matched:
            github_links = git_link_matched
            data["github"]["profile_url"] = exact_link

    data["github"]["username"] = github_links[0]


def get_passout_year(text):
    years = [1, 0, 10, 2]
    soup = BeautifulSoup(text, features="html.parser")
    divs = soup.find(education_type="college")
    for div in divs:
        match = re.findall(r'([2][0-9]{3})', div.getText())
        if len(match) > 0:
            for year in match:
                years.append(int(year))

    years.sort()
    data["passout_year"] = years[len(years) - 1]


def get_github_stats(username):
    github_page = urlopen(f"https://github-readme-stats.vercel.app/api?username={username}")
    commit_soup = BeautifulSoup(github_page.read(), features="html.parser")
    texts = commit_soup.find_all("text")

    for text in texts:
        if text.get("data-testid") == "commits":
            data["github"]["commits"] = int(text.get_text())


login(internshala_username, internshala_password)
navigate_to_edit_resume()
add_position("Jr_DEV")
time.sleep(15)

driver.get(driver.current_url)

page_content = driver.find_element(By.TAG_NAME, "html").get_attribute("outerHTML")

get_passout_year(page_content)
get_github_username(page_content)
get_github_stats(data["github"]["username"])
print(data)
