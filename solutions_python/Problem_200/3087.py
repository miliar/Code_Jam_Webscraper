def set_to_9(digits, i):
    if i > 0 and digits[i] == digits[i-1]:
        set_to_9(digits, i-1)
    else:
        digits[i] -= 1
        for j in range(i + 1, len(digits)):
            digits[j] = 9
    return digits

with open("B-large.in") as f:
    with open("B-large.out", "w") as out:
        for (l, line) in enumerate(f):
            if l == 0:
                continue
            digits = [int(char) for char in line.rstrip()]
            for i in range(1, len(digits)):
                if digits[i-1] > digits[i]:
                    digits = set_to_9(digits, i-1)
                    break
            num = int("".join(map(str, digits)))
            out.write("Case #{}: {}\n".format(l, num))
