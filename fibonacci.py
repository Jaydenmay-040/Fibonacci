# function using nth fibonacci
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # first fibonacci number is 0
    elif n == 0:
        return 0
    # second fibonacci is 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for x in range(20):
    print(fibonacci(x), end = " ")