'''Tests for pal.py'''
from pal import is_pal

def test_empty():
    '''Empty string is a palindrome'''
    assert is_pal('')


def test_single():
    '''Single character is a palindrome'''
    assert is_pal('a')
    assert is_pal('x')

