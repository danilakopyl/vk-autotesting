import pytest
import math


def square(n):
    return n * n


def square_root(n):
    return n**(1/2)


def get_int(n: float):
    return math.modf(n)[1]


def tuples_sum(a: tuple, b: tuple):
    return tuple(map(lambda x, y: x + y, a, b))


# float test 1
def test_float_square():
    assert square(1.5) == 2.25


# float test 2
def test_float_square_root():
    assert square_root(6.25) == 2.5


# float test 3
def test_float_get_decimal():
    assert get_int(2.65) == 2


# tuple test 1 parametrized
@pytest.mark.parametrize(('input', 'output'), ((2, 4), (-3, 9)))
def test_square(input, output):
    assert square(input) == output

# tuple test 2


def test_tuples_sum():
    tuples = [(1, 2), (10, 20)]
    expected = (11, 22)
    assert tuples_sum(*tuples) == expected


# tuple test 3 expected negative
def test_type_error():
    # with pytest.raises(TypeError):
    #    tuples_sum((1, 2), (1, 'a'))
    try:
        tuples_sum((1, 2), (1, 'a'))
        assert False
    except TypeError:
        assert True
