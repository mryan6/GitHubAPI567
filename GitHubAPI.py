"""
  Michael Ryan
  SSW-567 HW-04a
  This script will use the GitHub API to return the names of a specific user's repos and the number of commits to each one
"""

import requests
import json

def getResponse(username) :
    url = 'https://api.github.com/users/'+username+'/repos'
    return requests.get(url)

def getRepos(response) :
    names = []
    if response :
        repos = json.loads(response.text)
        for repo in repos :
            names.append(repo['name'])

    return names

def getCommits(username, repos) :
    if (len(repos) > 0) :
        for repo in repos :
            commits = json.loads(requests.get('https://api.github.com/repos/'+username+'/'+repo+'/commits').text)
            print ('Repo: '+repo+' commits: '+str(len(commits)))

        return True
    else :
        return False



def main():
    name = input('Please enter your GitHub username: ')
    response = getResponse(name)
    if response :
        repos = getRepos(response)
        getCommits(name,repos)

    else :
        print('Error connecting with API')

if __name__ == "__main__":
    main()
