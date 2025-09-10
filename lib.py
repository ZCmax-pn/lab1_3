def count_common_elements(*lists):
    """
    Принимает N списков и возвращает количество одинаковых элементов в них.
    """
    if not lists:
        return 0
    # Преобразуем первый список во множество
    common = set(lists[0])
    # Пересекаем со всеми остальными
    for lst in lists[1:]:
        common &= set(lst)
    return len(common)


if __name__ == "__main__":
    # Пример
    print(count_common_elements([1, 2, 3], [2, 3, 4], [0, 2, 3, 5]))
    # Ожидаемый результат: 2 (элементы 2 и 3 есть во всех списках)
