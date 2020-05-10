#!/usr/bin/env python

from github import Github
import pandas as pd
import time

import argparse

# required arg

parser = argparse.ArgumentParser()

parser.add_argument('--org', required=True)
parser.add_argument('--tocken', required=True)


args = parser.parse_args()



tocken = args.tocken
organization = args.org



results = {}
g = Github(tocken)


#for repo in g.get_user().get_repos():
 #   print(repo.name)

i = 1
while True:

    for repo in g.get_organization(organization).get_repos():
        print(repo.name)
        if repo.name not in results.keys():
            results[repo.name] = []
        try:
            results[repo.name].append([repo.get_contributors().totalCount, repo.get_commits().totalCount])
        except Exception as e:
            print(e)

    with open('my_html.html', 'w') as f:
        pd.DataFrame(results).to_html(f)
    i += 1
    print('Start sleeping 60 mins')
    time.sleep(360)