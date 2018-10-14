t = int(input())

for i in range(1, t + 1):
    integer = int(input())
    while True:
        if integer == int("".join((sorted(str(integer))))):
            break
        integer -= 1

    print("Case #{}: {}".format(i, integer))


