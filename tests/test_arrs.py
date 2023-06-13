from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_get_out_of_bounds():
    assert arrs.get([1, 2, 3], 10, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_my_slice_out_of_bounds():
    assert arrs.my_slice([1, 2, 3], 0, 10) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -10, 2) == [1, 2]
    assert arrs.my_slice([1, 2, 3], -1, 2) == []
    assert arrs.my_slice([], -10, 2) == []
