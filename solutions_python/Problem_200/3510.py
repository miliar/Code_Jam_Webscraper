t = int(input())

for i in range(1, t + 1):
    number = int(input())

    testing = True
    while testing and number>0:
        digits = list(str(number))
        ordered = list(str(number))
        ordered.sort()
        if digits == ordered:
            testing = False
        else:
            number -= 1
    print("Case #{}: {}".format(i, number))
