#!/usr/bin/env python3
"""
Module test_utils
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for test_access_nested_map()
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map with key path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for get_json()"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, payload):
        """Should return expected result"""
        with patch('utils.get_json', return_value=payload) as mock:
            res = mock(url)
            mock.assert_called_once_with(url)
