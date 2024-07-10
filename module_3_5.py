# Рекурсия
def get_multiplied_digits(number):
    p = 1
    if number < 10:
        return number
    str_number = str(number)
    first = int(str_number[0])
    return p * first * get_multiplied_digits(int(str_number[1:]))

# Исходный код:
result = get_multiplied_digits(40203)
print(result)

# Вывод на консоль:
# 24