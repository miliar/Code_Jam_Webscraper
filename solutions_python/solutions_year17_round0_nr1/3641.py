import sys

file_name = "A-large"

sys.stdin = open(file_name + ".in")
sys.stdout = open(file_name + ".out", "w")

number_of_test_cases = int(input())


def check_if_happy(cakes):
    i = 0
    for sid in cakes:
        if sid == '+':
            i += 1
    if i == len(cakes):
        return True
    else:
        return False


def flip_size(side):
    if cakes_list[side] == '-':
        cakes_list[side] = '+'
    else:
        cakes_list[side] = '-'

for testCase in range(1, number_of_test_cases + 1):
    case = input().split()
    S = case[0]
    cakes_list = list(S)
    K = int(case[1])
    if check_if_happy(cakes_list):
        print("Case #" + str(testCase) + ": 0")
        continue
    if len(cakes_list) < K:
        print("Case #" + str(testCase) + ": IMPOSSIBLE")
        continue
    number_of_flip = 0
    for c in range(0, len(cakes_list)):
        non_happy = cakes_list.index('-')
        if non_happy > (len(cakes_list) - K):
            print("Case #" + str(testCase) + ": IMPOSSIBLE")
            break
        else:
            for x in range(non_happy, non_happy + K):
                flip_size(x)
            number_of_flip += 1
        if check_if_happy(cakes_list):
            print("Case #" + str(testCase) + ": " + ("%d" % number_of_flip))
            break
