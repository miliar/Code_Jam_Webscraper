def solve(inputs):
    n = len(inputs)
    x = inputs[0]
    s1 = 0
    for (x, y) in zip(inputs, inputs[1:]):
        if y - x <= 0:
            s1 += y - x

    s1 = abs(s1)

    s2 = 0
    max_d = 0
    for (x, y) in zip(inputs, inputs[1:]):
        if y - x <= 0:
            max_d = min(y - x, max_d)

    max_d = abs(max_d)

    for x in inputs[0:-1]:
        if x <= max_d:
            s2 += x
        else:
            s2 += max_d

    return str(s1) + ' ' + str(s2)


if __name__ == "__main__":
    testcases = int(input())

    for caseNr in range(1, testcases + 1):
        x = input()
        inputs = [int(x) for x in input().split(' ')]
        print("Case #%i: %s" % (caseNr, solve(inputs)))