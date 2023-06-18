from testpage import get_title, create_post, delete

def test_step1_get(title):
    """Проверяем на вхождение ожидаемого результата в полученный ответ"""
    assert title in get_title()

def test_step2_post(text1):
    """Сравниваем ожидаемый статус код с полученным"""
    assert text1 == create_post()

def test_step3_delete(text2):
    """Сравниваем ожидаемый результат отработки метода DELETE с полученным"""
    assert text2 == delete()
