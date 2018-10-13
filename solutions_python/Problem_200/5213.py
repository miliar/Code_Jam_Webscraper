with open('B-small-attempt5.in', 'r') as prac_file:
    lines = prac_file.readlines()

testcases = int(lines[0])
tests = [int(lines[l].strip('\n')) for l in range(1, testcases + 1)]
output = []
for t, test in enumerate(tests):
    digits = [int(i) for i in str(test)]
    for i, d in enumerate(digits):
        if i > 0:
            if digits[i] < digits[i - 1]:
                # not tidy

                if digits[i - 1] == digits[i - 2] and i - 2 >= 0:
                    if t == 12:
                        print i
                        print digits
                    while digits[i - 1] == digits[i - 2]:
                        i -= 1
                    i -= 1
                    digits[i] -= 1
                    i += 1
                    for j in range(i, len(digits)):
                        digits[j] = 9
                    break
                else:

                    digits[i - 1] = digits[i - 1] - 1

                    for j in range(i, len(digits)):
                        digits[j] = 9
                    break
    st = ""
    if digits[0] == 0:
        digits = digits[1:]
    for d in digits:
        st += str(d)
    output.append("Case #{}: {}\n".format(t + 1, st))
    with open('B-small-attempt0.out', 'w') as out:
        for i, o in enumerate(output):
            if i == len(output) -1:
                o = o.strip('\n')
            out.write(o)
