import math

for t in range(int(input())):
    print("Case #%s: " % str(t + 1), end="")
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    l = int(math.log(k, 2))
    level_sum = (n - 2 ** l + 1)
    space = level_sum // 2 ** l
    if k - 2 ** l >= level_sum % 2 ** l:
        space -= 1
    mins = space // 2
    print(space - mins, mins)
