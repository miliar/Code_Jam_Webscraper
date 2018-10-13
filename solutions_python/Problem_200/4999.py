## GCJ 2017 B
import fileinput
import sys
from itertools import islice
f = open("stdout1.txt", "w")
sys.stdout = f
with open("B-small-attempt7.in") as fin:
    tidy = []
    t = 0
    for line in islice(fin,1,101):
        t = t + 1
        y = int(line)
        for i in range(1,y+1):
            if i < 10:
                tidy.append(i)
            else:
                x = str(i)
                if x[-1] < x[-2]:
                    pass
                elif (x[1] >= x[0]) and (x[-1] >= x[-2]) and (x[-1] >= x[0]):
                    tidy.append(i)
        m = tidy[-1]
        sys.stdout.write("Case #{}: {}".format(t , m) + "\n")

# t = int(input())  # read a line with a single integer
# for i in range(1, t + 1):
#     m = tidy[-1]
# print("Case #{}: {}".format(i, m))
