import requests
import os

USERS = ["erezcarmel", "erezc-wand"]
TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_github_stats(user):
    url = f"https://api.github.com/users/{user}"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching {user} stats:", response.json())
        return None

merged_data = {"public_repos": 0, "followers": 0, "stars": 0}
for user in USERS:
    data = fetch_github_stats(user)
    if data:
        merged_data["public_repos"] += data["public_repos"]
        merged_data["followers"] += data["followers"]

README_CONTENT = f"""
# GitHub Stats Merged

👤 Combined Stats for `{USERS[0]}` & `{USERS[1]}`

- 📦 **Total Public Repos:** {merged_data["public_repos"]}
- 👥 **Total Followers:** {merged_data["followers"]}

_Updated automatically using GitHub Actions 🚀_
"""

# Write to README.md
with open("README.md", "w") as file:
    file.write(README_CONTENT)
