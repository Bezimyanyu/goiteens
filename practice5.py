num_1: int =int(input("Введіть перше число: "))
num_2: int =int(input("Введіть друге число: "))
num_3: int =int(input("Введіть третє число: "))


if num_1 % 2 == 0:
    print("Перше число парне")
else:
    print("Перше число не парне")

if num_2 % 2 == 0:
    print("Друге число парне")
else:
    print("Друге число не парне")

if num_3 % 2 == 0:
    print("Третє число парне")
else:
    print("Третє число не парне")

num_1k=(num_1 ** 2)
num_2k=(num_2 ** 2)
num_3k=(num_3 ** 2)

if num_1k > 100:
    print("Перше число у квадраті більше 100")
else:
    print("Я не знаю що це за число")

if num_2k > 100:
    print("Друге число у квадраті більше 100")
else:
    print("Я не знаю що це за число")

if num_3k > 100:
    print("Третє число у квадраті більше 100")
else:
    print("Я не знаю що це за число")
