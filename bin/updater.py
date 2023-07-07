#!/usr/bin/env python3
import json
import os
import re

from github import Auth, Github

GH_ACCESS_TOKEN = os.getenv("GH_ACCESS_TOKEN")
g = Github(auth=Auth.Token(GH_ACCESS_TOKEN)) if GH_ACCESS_TOKEN else Github()


def update_projects_json():
    with open(".gitmodules", "rt") as f:
        content = f.read()

    data = []
    p = re.compile(r"github.com:(.*)\.git")
    print("Updating projects ...")
    for x in re.findall(p, content):
        repo = g.get_repo(x)
        data.append(
            {
                "name": repo.name,
                "repo_url": repo.svn_url,
                "home_url": repo.homepage,
                "desc": repo.description,
                "tags": repo.topics,
                "github_stars": repo.stargazers_count,
            }
        )
    data = sorted(data, key=lambda x: x["github_stars"], reverse=True)

    with open("projects.json", "w") as write_file:
        json.dump(data, write_file, indent=4, sort_keys=True)

    print("Update successful")


def update_readme():
    with open("projects.json", "rt") as f:
        data = json.load(f)

    entries = []
    for i, d in enumerate(data, start=1):
        name = f'**{d["name"]}**'
        repo = f'[Repo]({d["repo_url"]})'
        home = f', [Home]({d["home_url"]})' if d["home_url"] else ""
        tags = f'`({", ".join(d["tags"])})`' if d["tags"] else ""
        entries.append(f'{i}. {name} - ({repo}{home}) {d["desc"]}{tags}')

    with open("templates/README.tmpl.md", "rt") as f:
        readme = f.read()
    readme = readme.replace("{APPS_LIST}", "\n".join(entries))
    with open("README.md", "wt") as f:
        f.write(readme)

    print("Updated README.md")


def main():
    update_projects_json()
    update_readme()


if __name__ == "__main__":
    main()
