f = open('/home/michael/Dropbox/Code Jam/2012/Dancing/InrealL.in')
numcases = int(f.readline())
for a in range(numcases):
    print "Case #%d:" % (a+1),
    line = f.readline().split()
    N = int(line[0])
    S = int(line[1])
    s = 0
    p = int(line[2])
    scores = line[3:]
    scores = map(int, scores)
    result = 0
    for score in scores:
        if (score % 3) == 2:
            high = score//3 + 1
            if high == p or high > p:
                result += 1
            if (high == (p-1)) and (s < S):
                result += 1
                s += 1
        if ((score % 3) == 0):
            if score != 0:
                high = score / 3
                if (high == p) or (high > p):
                    result += 1                
                if (high == (p-1)) and (s < S):
                    result += 1
                    s += 1
            else:
                if p == 0:
                    result += 1
        if (score % 3) == 1:
            high = score // 3
            high += 1
            if (high == p) or (high > p):
                result += 1
    print result
