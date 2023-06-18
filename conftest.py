import pytest

@pytest.fixture()
def title():
    """Возвращаем ожидаемый результат для метода GET"""
    return "qui est esse"
@pytest.fixture()
def text1():
    """Возвращаем ожидаемый результат для метода POST"""
    return 201
@pytest.fixture()
def text2():
    """Возвращаем ожидаемый результат для метода DELETE"""
    return {}
