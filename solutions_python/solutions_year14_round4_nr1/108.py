# Python 3.2

from common import *

def main(casenum):
    n, x = readints()
    s = readints()
    # s = []
    # for i in range(n):
        # s.append(readint())

    used = [False] * n

    # i_ = n - 1
    # while (i_ > 0) and s[i_] * 2 > x:
        # i_ -= 1

    s.sort()

    i = n - 1
    count = 0
    while i >= 0:
        if used[i]:
            i -= 1
            continue
        count += 1
        used[i] = True
        j = i - 1
        while (j >= 0) and (used[j] or (s[j] + s[i] > x)):
            j -= 1
        if j >= 0:
            used[j] = True
        i -= 1

    writeline('Case #{}: {}'.format(casenum, count))

run(main)
