import math

num = int(raw_input())
for i in range(1, num+1):
    tmp = raw_input().split()
    pans = list(tmp[0])
    n = int(tmp[1])

    count = 0
    for j in range(len(pans) - n + 1):
        if pans[j] == "-":
            count += 1
            for k in range(n):
                if pans[j + k] == "-":
                    pans[j + k] = "+"
                else:
                    pans[j + k] = '-'

    imp = False
    for j in range(len(pans)):
        if pans[j] == "-":
            imp = True
            break

    if not imp:
        print "Case #%d: %d" %(i, count)
    else:
        print "Case #%d: IMPOSSIBLE" %(i)
