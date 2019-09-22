"""
  Michael Ryan
  SSW-567 HW-04a
  This file will be used to unit test the implementation of our GitHubAPI requests
"""

import unittest
import requests
from GitHubAPI import getRepos, getCommits, getResponse

class TestGitHub(unittest.TestCase):

    def testGetResponse(self) :
        self.assertEqual(getResponse('mryan6').status_code, 200, 'mryan6 is a valid GitHub username, therefore it should return with status code 200')

    def testGetBadResponse(self) :
        self.assertNotEqual(getResponse('').status_code, 200, 'This is not a valid GitHub username, therefore it should not return with status code 200')

    def testGetRepos(self) :
        response = getResponse('mryan6')
        repos = getRepos(response)
        self.assertEqual(len(repos), 7, 'My own GitHub username has 7 repos associated with it')

    def testGetBadRepos(self) :
        response = getResponse('')
        repos = getRepos(response)
        self.assertEqual(len(repos),0,'This GitHub username does not exist therefore there are no repos to return')

    def testGetCommits(self) :
        response = getResponse('mryan6')
        repos = getRepos(response)
        commits = getCommits('mryan6',repos)
        self.assertEqual(commits,True,'My own GitHub has repos with commits associated with it')

    def testGetBadCommits(self) :
        response = getResponse('')
        repos = getRepos(response)
        commits = getCommits('',repos)
        self.assertEqual(commits,False,'This GitHub username does not exist and therefore there are no commits to return')
