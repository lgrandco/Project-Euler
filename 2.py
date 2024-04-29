r = 0
a, b = 1, 2
while b < 4000000:
    if not b % 2:
        r += b
    a, b = b, a + b

print(r)
