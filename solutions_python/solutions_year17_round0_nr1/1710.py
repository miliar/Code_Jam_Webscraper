# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# 3
# --+-++- 3
# +++++ 4
# -+-+-+ 4
import re
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = input()
    (pancakes, k) = s.split()
    k = int(k)
    #print(s)
    row = []
    for c in pancakes:
        row.append(c=='+'),
#    print("Case #{}: {}".format(i, len(s)))
    #print("Case #{}: INPUT k{} p{} row{}".format(i, k, pancakes, row))
    n = 0
    for j in range(0, len(row)-k+1):
        #print("j:%d row:%s" % (j, row))
        if not row[j]:
            # flip
            for j_ in range(j, j+k):
                row[j_]=not row[j_]
            #print("flipped")
            n += 1
    unflipped = [not i for i in row]
    if any(unflipped):
        n = 'IMPOSSIBLE'
    print("Case #{}: {}".format(i, n))