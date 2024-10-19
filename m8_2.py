# ================================ sum num ================================
def personal_sum(numbers):
    result = 0
    incorrect = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect += 1
            print(f'Некорректный тип данных для подсчёта суммы {num}')
    return (result, incorrect)

# ================================ average ================================
def calculate_average(numbers):
    try:
        result, incorrect = personal_sum(numbers)
        num_of_nums = len(numbers) - incorrect
        average = result / num_of_nums
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return


# ================================= test case ===============================
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать