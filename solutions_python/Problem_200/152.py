import sys

name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input().split()

    N = line[0]
    res = list(N)

    last_digit = None
    remainder = False
    x = 0

    while x < 20:
        for i, char in enumerate(N):
            digit = int(char)
            if not last_digit:
                last_digit = digit
                continue
            if digit >= last_digit:
                last_digit = digit
                continue
            last_digit = digit
            for j in range(i, len(res)):
                res[j] = '9'
            if res[i] != '0':
                res[i-1] = str(int(res[i-1]) - 1)
            else:
                j = i - 1
                while res[j] == '0':
                    res[j] = '9'
                    j -= 1
                res[j] -= 1
            break

        last_digit = None
        N = ''.join(res)
        x += 1



    print("Case #" + str(testCase) + ": " + ("%s" % (''.join(res)).lstrip('0')))