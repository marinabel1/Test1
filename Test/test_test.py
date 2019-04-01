class TestSuite():

    def test_case_1(self, case, model):
        """Проверка, что заданная длина списка равна 5"""
        a = [1, 2, 5, 9, 12]
        assert(len(a) == 5)

    def test_case_2(self, case):
        """Проверка, что сложенные две строки соответствуют ожидаемому результату"""
        stroka1 = "Hello "
        stroka2 = "World"
        stroka3 = stroka1 + stroka2
        assert(stroka3 == "Hello World")

    def test_case_3(self, case):
        """Проверка, что уравнение 3+2*1 равно 5"""
        assert(3 + 2 * 1 == 5)

    def test_case_4(self, case):
        """Проверка, что элемент из списка удален успешно"""
        b = ["one", "two", "three"]
        b.remove("two")
        assert(b == ["one", "three"])

    def test_case_5(self, case):
        """Проверка, что переменные поменялись значениями"""
        e = (99, 98, 97, 96)
        t = (1, 2, 3, 4)
        e, t = t, e
        assert t == (99, 98, 97, 96)