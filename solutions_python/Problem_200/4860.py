#!/usr/bin/python3

import fileinput

"""
    GCJ: Tidy Numbers
"""

f = fileinput.input()
NO_OF_CASES = int(f[0])
tidy_num: int
case = 1

# iterating for each case
for line in f:
    string = line.strip('\n')
    num = int(string)
    status = False
    ans = 0
    n = 0

    # iterating for each number
    if len(string) == 1:
        print("Case #{}: {}".format(case, string))
        case += 1
        continue

    if int(string) <= 20:
        print("Case #{}: {}".format(case, num-1))
        case += 1
        continue

    for i in range(num+1):
        for j in range(len(str(i)) - 1):
            if str(i)[j] <= str(i)[j + 1]:
                status = True
            else:
                status = False
                break

        if status:
            ans = i

    print("Case #{}: {}".format(case, ans))
    case += 1
