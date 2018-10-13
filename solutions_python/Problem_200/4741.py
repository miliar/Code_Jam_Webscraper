import sys

name = "A-small"
path = ""

path2 = '/Users/daniel/Downloads/B-small-attempt0'

sys.stdin = open(path2 +'.in')
sys.stdout = open(path2 + ".out", "w")

testCases = int(input())


def check_non_decreasing(num):
    num = str(num)
    prev_d = num[0]
    for d in range(1, len(num)):
        if int(num[d]) >= int(prev_d):
            prev_d = num[d]
            continue
        return False
    return True


for testCase in range(1, testCases + 1):
    str_input = str(input())
    highest = 1
    for i in range(int(str_input) + 1):
        if check_non_decreasing(i):
            highest = i

    print('Case #{}: {}'.format(testCase, highest))