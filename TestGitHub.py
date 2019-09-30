"""
  Michael Ryan
  SSW-567 HW-04a
  This file will be used to unit test the implementation of our GitHubAPI requests
"""

import unittest
import requests
import GitHubAPI
import json
from unittest.mock import patch, Mock
from GitHubAPI import getRepos, getCommits, getResponse

class TestGitHub(unittest.TestCase):
    @patch('GitHubAPI.requests.get')
    def testGetResponse(self, mock_get) :
        mock_get.return_value.status_code = 200
        response = getResponse('mryan6')
        self.assertEqual(response.status_code, 200, 'mryan6 is a valid GitHub username, therefore it should return with status code 200')

    @patch('GitHubAPI.requests.get')
    def testGetBadResponse(self, mock_get) :
        mock_get.return_value.status_code = 404
        response = getResponse('')
        self.assertNotEqual(response.status_code, 200, 'This is not a valid GitHub username, therefore it should not return with status code 200')

    @patch('GitHubAPI.requests.get')
    @patch('GitHubAPI.requests.Response')
    @patch('GitHubAPI.getRepos')
    def testGetRepos(self, mock_get_repos, mock_response, mock_get) :
        repos = [{
            "name" : "GitHubAPI567"},
            {"name" : "helloworld"},
            {"name" : "HW-01"},
            {"name" : "IntroToAIFinalProject"},
            {"name" : "ssw-322-maze"},
            {"name" : "SSW555-Project-02"},
            {"name" : "SSW567-HW-02"
        }]
        mock_response.text = Mock(text=json.dumps(repos)).text
        mock_get.return_value.status_code = 200
        mock_get.return_value.text.return_value = json.dumps(repos)
        mock_get_repos.return_value = Mock()
        mock_get_repos.return_value.json.return_value = json.dumps(repos)
        response = getResponse('mryan6')
        length = len(getRepos(mock_response))
        self.assertEqual(length, 7, 'My own GitHub username has 7 repos associated with it')

    @patch('GitHubAPI.requests.get')
    @patch('GitHubAPI.requests.Response')
    @patch('GitHubAPI.getRepos')
    def testGetBadRepos(self, mock_get_repos, mock_response, mock_get) :
        repos = []
        mock_response.text = Mock(text=json.dumps(repos)).text
        mock_get.return_value.status_code = 200
        mock_get.return_value.text.return_value = json.dumps(repos)
        mock_get_repos.return_value = Mock()
        mock_get_repos.return_value.json.return_value = json.dumps(repos)
        response = getResponse('')
        repos = getRepos(mock_response)
        self.assertEqual(len(repos),0,'This GitHub username does not exist therefore there are no repos to return')

    @patch('GitHubAPI.requests.get')
    @patch('GitHubAPI.requests.Response')
    @patch('GitHubAPI.getCommits')
    def testGetCommits(self, mock_get_commits, mock_response, mock_get) :

        repos = ["GitHubAPI567", "helloworld", "HW-01", "IntroToAIFinalProject", "ssw-322-maze", "SSW555-Project-02", "SSW567-HW-02"]
        commits = [
            {"GitHubAPI567" : 7},
            {"helloworld" : 6},
            {"HW-01" : 5},
            {"IntroToAIFinalProject" : 4},
            {"ssw-322-maze" : 3},
            {"SSW555-Project-02" : 2},
            {"SSW567-HW-02" : 1}
        ]
        mock_response.text = Mock(text=json.dumps(commits)).text
        mock_response.return_value = json.dumps(commits)
        mock_get.return_value = mock_response
        mock_get.return_value.status_code = 200
        mock_get_commits.return_value.json.return_value = json.dumps(commits)
        found_commits = getCommits('mryan6',repos)
        self.assertEqual(found_commits,True,'My own GitHub has repos with commits associated with it')

    @patch('GitHubAPI.requests.get')
    @patch('GitHubAPI.requests.Response')
    @patch('GitHubAPI.getCommits')
    def testGetBadCommits(self, mock_get_commits, mock_response, mock_get) :
        repos = []
        commits = []
        mock_response.text = Mock(text=json.dumps(commits)).text
        mock_response.return_value = json.dumps(commits)
        mock_get.return_value = mock_response
        mock_get.return_value.status_code = 200
        mock_get_commits.return_value.json.return_value = json.dumps(commits)
        commits = getCommits('',repos)
        self.assertEqual(commits,False,'This GitHub username does not exist and therefore there are no commits to return')
