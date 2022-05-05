#!/usr/bin/env python3
"""
Module test_utils
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


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
