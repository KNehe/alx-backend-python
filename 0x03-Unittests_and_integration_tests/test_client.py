#!/usr/bin/env python3
"""
Module test_client
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """test for client.GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock):
        """test org returns correct value"""
        test_class = GithubOrgClient(org_name)
        value = test_class.org

        self.assertEqual(value, mock.return_value)

        mock.assert_called_once()

    @parameterized.expand([
        ("django", {"repos_url": "django"})
        ])
    def test_public_repos_url(self, name, expected):
        """test_public_repos_url"""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value=expected
                          ) as mock:
            test_class = GithubOrgClient(name)
            return_value = test_class._public_repos_url

            self.assertEqual(return_value,
                             mock.return_value.get('repos_url'))
            mock.assert_called_once()
