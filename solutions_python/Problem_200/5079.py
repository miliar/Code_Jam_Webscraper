n = int(input())

for tc in range(1, n + 1):
    base = list(str(int(input())))

    if int(''.join(base)) < int(base[0] * len(base)):
        base = int(str(int(base[0])) + (len(base)-1)*"0") - 1
        base = list(str(base))
        
        # This also has the be the nearest tidy number
    else:
        for i in range(len(base) - 1):
            # If the next digit is less than the currnt digit
            # the number is not tidy
            # so we adjust the base
            if int(base[i+1]) < int(base[i]):
                base[i] = str(int(base[i]) -1)
                for j in range(i+1, len(base)):
                    base[j] = "9"

    print("Case #" + str(tc) + ":", ''.join(base))


