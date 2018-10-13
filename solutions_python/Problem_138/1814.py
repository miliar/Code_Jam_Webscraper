def rem(a, b):
    count = 0
    score = 0
    n = len(a)
    for x in a:
        if x < b[0]:
            count += 1
    '''import pdb
    pdb.set_trace()'''
    if count == n:
        return 0
    elif count==0:
        a = a[1:n]
        b = b[1:n]
        score = score + 1 + rem(a, b)
    else:
        a = a[count:n]
        b = b[0:n-count]
        score = score + rem(a, b)
    return score
str = "D-small-attempt1.in"
fo = open(str, "r");
T = int(fo.readline());
for i in range(T):
    n = int(fo.readline())
    x1 = fo.readline().strip().split(" ")
    x2 = fo.readline().strip().split(" ")
    y1 = [float(x) for x in x1]
    y2 = [float(x) for x in x2]
    y1.sort()
    y2.sort()
    y3 = y2[:]
    score2 = 0
    for x in y1:
        if x > y3[-1]:
            score2 += 1
            y3.remove(y3[0])
            continue
        for y in y3:
            if x < y:
                y3.remove(y) 
                break
    score1 = rem(y1,y2)
    print "Case #%d: %d %d" %(i+1, score1, score2)

