# test_main.py
from main import add

def test_add_positive_numbers():
    """测试两个正数相加"""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """测试两个负数相加"""
    assert add(-1, -1) == -2
