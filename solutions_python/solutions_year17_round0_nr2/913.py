T = int(raw_input())

for case in range(1, T+1):
    digits = map(int, list(str(int(raw_input().strip()))))
    no_digits = len(digits)
    if no_digits < 2:
        print "Case #{}: {}".format(case, "".join(map(str, digits)))
    else:
        for _ in range(no_digits):
            force_9 = False
            for digit_index in range(no_digits-1):
                if force_9:
                    digits[digit_index] = 9
                    continue

                if digits[digit_index] <= digits[digit_index+1]:
                    continue
                elif digits[digit_index] > 0:
                    digits[digit_index] -= 1
                    force_9 = True
                else:
                    digits[digit_index-1] -= 1
                    digits[digit_index] = 9
                    force_9 = True
            if force_9:
                digits[no_digits-1] = 9
        print "Case #{}: {}".format(case, int("".join(map(str, digits))))

