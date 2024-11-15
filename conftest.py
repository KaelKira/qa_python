import pytest

# класс Company, в котором реализован конструктор и методы
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector