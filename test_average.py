import pytest
from average import average

def test_basic():
    assert average([1, 2, 3]) == 2

def test_single_value():
    assert average([5]) == 5

def test_empty_list_edge_case():
    with pytest.raises(ValueError):
        average([])
