def f(n, x):
    a = n // x * x
    return (a * (a + x) // x) >> 1


def solve(n):
    return f(n - 1, 3) + f(n - 1, 5) - f(n - 1, 15)


print(solve(1000))
