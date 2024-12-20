#Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.

#Не забудьте, що перший елемент масиву має індекс 0.

#Для порожнього масиву результат завжди 0.

#Пояснення:



##[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

#[1, 3, 5] => 30
#[6] => 36
#[] => 0
#Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.


numbers=["[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88]",
         "[1, 3, 5] => 30",
         "[6] => 36",
         "[] => 0"
]


def calculate(numbers):
    if not numbers:  # Если список пустой, возвращаем 0
        return 0

    # Суммируем элементы с четными индексами
    even_index_sum = 0  # Переменная для хранения суммы элементов с четными индексами
    for i in range(0, len(numbers), 2):  #  по четным индексам
        even_index_sum += numbers[i]

    # Умножаем сумму на последний элемент списка
    return even_index_sum * numbers[-1]  # Итоговое значение возвращается


# Примеры для проверки
print(calculate([0, 1, 7, 2, 4, 8]))  # (0 + 7 + 4) * 8 = 88
print(calculate([1, 3, 5]))  # (1 + 5) * 5 = 30
print(calculate([6]))  # 6 * 6 = 36
print(calculate([]))  # Пустой список, результат 0
