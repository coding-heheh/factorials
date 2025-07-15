def factorial(x):
    if x == 1:
        return 1
    elif x < 0:
        return 0
    else:
        return (x * factorial(x-1))

num = int(input("enter a number: "))
print(f'the factorial of {num} is {factorial(num)}')


