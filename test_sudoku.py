import pytest
from sudoku import check




def test_check():
    assert check([1,2,3,4,5,6,7,8,9]) == True
    assert check([1,2,4,4,5,3,7,8,9]) == False
    assert check([1,2,0,4,5,3,0,8,9]) == False