def countFlips(s, k):
    flips = 0
    slist = list(s)
    for i in range(len(slist)):
        if slist[i] == '-':
            flips += 1
            for j in range(i + k):
                if j >= len(slist):
                    flips = -1
                else:
                    if slist[j] == '-':
                        slist[j] = '+'
                    else:
                        slist[j] = '-'

    if flips == -1:
        return "IMPOSSIBLE"
    else:
        return flips


test_cases = int(raw_input())

for case in xrange(1, test_cases + 1):
    s, k = [data for data in raw_input().split(" ")]
    print "Case #{}: {}".format(case, countFlips(s, int(k)))
