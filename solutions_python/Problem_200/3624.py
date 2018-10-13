def is_tidy(s):
    c_prev = int(s[0])
    for c in map(int, s):
        if c_prev > c:
            return False
        c_prev = c
    return True


t = int(input())
for i in range(1, t + 1):
    s = input()
    digits = [int(c) for c in s]

    for j in range(len(digits) - 1, 0, -1):  # Iterate from right to left
        if digits[j] < digits[j - 1]:  # digit i is faulty
            digits[j - 1] -= 1
            digits[j:] = [9] * (len(digits) - j)

    print("Case #{}: {}".format(i, int(''.join(map(str, digits)))))  # Cheap concat + removal of leading 0's
