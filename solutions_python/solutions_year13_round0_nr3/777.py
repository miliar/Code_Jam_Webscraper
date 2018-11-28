T = raw_input()
T = int(T)

for t in xrange(1, T+1):
    A, B = raw_input().split()
    A = int(A)
    B = int(B)
    cnt = 0
    for i in xrange(1, B+1):
        s = str(i)
        x = 0
        if(i**2 >= A and i**2 <= B):
            for j in xrange(0, len(s)/2):
                if(s[j] != s[len(s)-j-1]):
                    x = 1
                    break
            if(x != 0):
                continue
            a = i**2
            s = str(a)
            for j in xrange(0, len(s)/2):
                if(s[j] != s[len(s)-j-1]):
                    x = 1
                    break
            if(x == 0):
                cnt+=1
    print "Case #%d: %d" % (t, cnt)
