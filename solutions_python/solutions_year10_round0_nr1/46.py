table=[2**i for i in xrange(0,31)]

def cal(nwidget, nsnap):
    res=nsnap%table[nwidget]
    if res==table[nwidget]-1:
        res="ON"
    else:
        res="OFF"
    return res

nc=input()
for i in xrange(nc):
    nwidget, nsnap=[int(t) for t in raw_input().split()]
    res=cal(nwidget, nsnap)
    print "Case #%d: %s" % (i+1, res)

