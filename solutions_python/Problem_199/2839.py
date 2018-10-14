t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    pancakes = list(line[0])
    n = len(pancakes)
    k = int(line[1])
    flips = 0
    for j in xrange(n-k+1):
        if pancakes[j] == '-':
            flips += 1
            for l in xrange(j, j+k):
                if pancakes[l] == '-':
                    pancakes[l] = '+'
                else:
                    pancakes[l] = '-'
    impossible = False
    for j in xrange(n-k+1, n):
        if pancakes[j] == '-':
            impossible = True
            break
    if impossible:
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
    else:
        print "Case #{}: {}".format(i, flips)

