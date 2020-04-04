x = 1
while x <= 9:
    y = 1
    while y <= x:
        print(y, "*", x, "=", y * x, " ", end=" ")
        y += 1
    print()
    x += 1
