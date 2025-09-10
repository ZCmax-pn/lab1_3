# test.py
from main import add_numbers

def test_add_numbers():
    # Тестируем сложение 2 + 3
    result = add_numbers(2, 3)
    assert result == 5, f"Ожидалось 5, получено {result}"
    print("Тест пройден!")

if __name__ == "__main__":
    test_add_numbers()