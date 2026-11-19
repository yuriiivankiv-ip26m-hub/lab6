import pytest
from main import calculate_discount


def test_normal_discount():
    assert calculate_discount(1000, 15) == 850.0


def test_no_discount():
    assert calculate_discount(1000, 0) == 1000.0


def test_full_discount():
    assert calculate_discount(1000, 100) == 0.0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)


def test_invalid_type():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)