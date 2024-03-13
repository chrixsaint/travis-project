# tests/test_my_script.py
from  ..import my_script  # Use two dots to go up one level

def test_add_numbers():
    assert my_script.add_numbers(2, 3) == 5
