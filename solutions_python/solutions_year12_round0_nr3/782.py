import sys

lines = sys.stdin.read().split("\n")
count = lines[0]

index = 1
s = None
for s in lines[1:-1]:
    LOWER, UPPER = map(int, s.split())
    good = []
    for j in range(LOWER, UPPER+1):
        s = str(j)
        tmp = s[1:] + s[0]
        i = int(tmp)
        while tmp != s:
            if i < j and i >= LOWER and i <= UPPER:
                good.append((i,j))
            tmp = tmp[1:] + tmp[0]
            i = int(tmp)

    print "Case #%d: %s" % (index, len(good))
    index += 1
