def verify(n):
    for k in xrange(0, len(n)-1,+1):
        if int(n[k]) > int(n[k+1]):
            return False

    return True
t=int(raw_input())
for i in xrange(1,t+1):
    n=raw_input()
    if int(n)==1:
        print "Case #" + `i` + ": " + n
    for j in xrange(int(n),1,-1):
        if verify(`j`):
            print "Case #"+`i`+": "+`j`
            break


