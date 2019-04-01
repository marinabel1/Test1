def test_case_6(case):
    """Проверка того, что две переменные не равны с разными значениями"""
    a = 10
    b = 20
    assert (a != b)

def test_case_7(case):
    """Проверка, что в словаре под индексом 1 находится значение 'жен' """
    pol = {0: 'муж',
           1: 'жен'}
    assert (pol[1] == 'жен')

def test_case_8(case):
    """Проверка, что после добавления нового элемента в список, количество элементов теперь равно 4"""
    p = ['IT', 'Developer', 'QA']
    p.append('DevOps')
    assert (len(p) == 4)

def test_case_9(case):
    """Проверка, того уравнение 2^3 равно 8"""
    assert (2**3 == 8)

def test_case_10(case, model):
    """Проверка того, что x = False """
    x = 0
    assert (x == False)