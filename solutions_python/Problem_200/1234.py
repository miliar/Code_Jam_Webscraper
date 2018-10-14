t = int(input())
count = 0
while t > 0:
    count += 1
    t -= 1
    n = list(input())
    old = 0
    violation = True

    while violation:
        # print("U: ", ''.join(n))
        old = 0
        for index in range(len(n)):
            digit = int(n[index])
            # print("L: ", ''.join(n))
            if digit >= old:
                # print("     NV: ", digit, old)
                old = digit
                violation = False

            else:
                # print("     V: ", digit, old)
                # fix violation
                # index = n.index(str(digit))
                a = int(n[index - 1]) - 1
                n[index - 1] = str(a)
                for i in range(len(n[index:])):
                    n[index + i] = '9'

                if a == 0 and index - 1 == 0:
                    n = n[1:]
                violation = True
                break

    print("Case #{count}: {result}".format(count=count, result=''.join(n)))
