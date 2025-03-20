def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Введите число для вычисления факториала: "))
print(f"Факториал числа {num} = {factorial(num)}")
a = 10