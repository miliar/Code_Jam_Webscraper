from __future__ import print_function
import sys

def tidy(t):
    for i in range(len(t)-1, -1, -1):
        lte = True
        for j in range(i, len(t)):
            if t[i] > t[j]:
                lte = False
                break
        if not lte:
            front = t[:i]
            middle = str(int(t[i]) - 1)
            end = '9' * (len(t) - i - 1)
            t = front + (middle if middle != "0" else "") + end
    return t

data = sys.stdin.readlines()

n = int(data[0])

for i in range(1, 1 + n):
    line = data[i].strip()
    print("Case #{}: {}".format(i, tidy(line)))
