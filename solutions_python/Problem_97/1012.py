__author__ = 'joker'
used = {}
def shifts(item, iitem):

    r = []
    for i in xrange(len(item)-1):
        t = item[i+1:] + item[:i+1];
        it = int(t)
        if len(str(it))==len(item) and not used.has_key((it,iitem)) and iitem!=it:
            r.append ( it )
            used[(it,iitem)] = True
            used[(iitem,it)] = True
    return r


N = int(raw_input())
for i in xrange(N):
    used.clear()
    a,b = [int(x) for x in raw_input().split(' ')]
    cnt = 0
    for item in range(a,b):
        for shift in shifts(str(item), item):
            if a <= shift <= b:
                #print "%d <= %d, %d <= %d" %(a,item, shift,b)
                cnt+=1
    print "Case #%d: %d" % (i+1, cnt)
