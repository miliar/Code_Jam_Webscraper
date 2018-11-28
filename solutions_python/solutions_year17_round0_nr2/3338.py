def assert_num(actual, expected):
    assert actual == expected, ("Expected ", expected, " got ", actual)


def backtracking(s, idx=0, previous=-1, nine=False):
    if idx >= len(s):
        return ""

    if nine:
        return "9" + backtracking(s, idx+1, 9, True)

    n = int(s[idx])

    result = None

    while result is None:
        if n < previous:
            return None
        result = backtracking(s, idx+1, n, nine)
        if result is None:
            n -= 1
            nine = True

    return str(n) + result



def answer_question(n):
    assert n >= 0, str(n) + " is less then zero"
    if n < 10:
        return n
    return int(backtracking(str(n)))


# assert_num(answer_question(1010), 1009)

with open("input.txt", "r") as handle:
    writer = open("output.txt", "w")
    handle.readline()
    idx = 1
    for x in handle:
        x = x[:-1]
        if len(x) == 0:
            continue
        func_out = str(answer_question(int(x)))
        answer = "Case #" + str(idx) + ": " + func_out
        print(idx, "-", x, func_out)
        writer.write(answer + "\n")
        idx += 1

assert_num(answer_question(4), 4)
assert_num(answer_question(132), 129)
assert_num(answer_question(1000), 999)
assert_num(answer_question(7), 7)
assert_num(answer_question(111111111111111110), 99999999999999999)
