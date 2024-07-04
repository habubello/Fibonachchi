def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib_prev, fib_current = 0, 1
        for i in range(2, n+1):
            fib_next = fib_prev + fib_current
            fib_prev, fib_current = fib_current, fib_next
        return fib_current

print(fibonacci(5))
# bu queryda nechi sonni yozsangiz ushani fibonacci boyicha chqarb beradi