import pytest


@pytest.fixture(scope='session', autouse=True)
def suite_data():
    print("\n ----------- Session start ---------------")
    yield
    print(">\n ----------- Session done ---------------")


@pytest.fixture(scope='function')
def case():
    print("\n   > Begin")
    yield
    print("\n   > End")

@pytest.fixture(scope='module', autouse=True)
def model():
    print("\n ----------- Module start ---------------")
    yield
    print(">\n ----------- Module done ---------------")


