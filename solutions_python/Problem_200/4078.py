t = int(input())

for i in range(1, t + 1):
    num_orig = int(input())

    for offset in range(0, num_orig):
        num = num_orig - offset

        digits = [int(x) for x in str(num)]

        last_digit = 0

        isTidy = True

        for j in range(0, len(digits)):
            if digits[j] >= last_digit:
                last_digit = digits[j]
            else:
                isTidy = False

                for k in range(j, len(digits)):
                    digits[k] = 0

                digits_map = map(str, digits)
                digits_map = ''.join(digits_map)
                digits_map = int(digits_map)

                num_orig = digits_map + offset

        if isTidy:
            print("Case #{}: {}".format(i, num))
            break
