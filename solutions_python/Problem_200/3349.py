from sys import argv


def is_tidy(n):
    if n < 10:
        return True
    elif n % 10 == 0:
        return False

    digits = [int(d) for d in str(n)]

    k = 0

    for l in range(1, len(digits)):
        if digits[k] > digits[l]:
            return False
        k = l

    return True


def get_next_number(n):
    digits = [int(d) for d in str(n)]
    factor = 10 ** (len(digits)-1)

    if digits[0] == 9:
        return (9 * factor) - 1

    if digits[-1] == 0:
        # 11110
        if len(set(digits)) == 2 and digits[1] == 1:
            return factor - 1
        return n - 1
    else:
        for k, m in enumerate(digits):
            if m > digits[k+1]:
                # change k+1 to 0
                idx = k+1
                while idx < len(digits):
                    digits[idx] = 0
                    idx = idx + 1
                break
        n = int(''.join(map(str, digits)))

    return n


if __name__ == '__main__':
    test_cases = open(argv[1])

    t = int(test_cases.readline())
    last_tidy = 1

    for i in range(1, t+1):
        n = int(test_cases.readline())
        current = n

        while True:
            if is_tidy(current):
                print(f"Case #{i}: {current}")
                break

            current = get_next_number(current)

    test_cases.close()
