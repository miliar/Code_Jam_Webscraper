def gcd(large,small):
    large=large%small
    if large==0:
        return small
    return gcd(small,large)


def cal(data):
    data=list(set(data))
    data.sort()
    dif=[data[i+1]-data[i] for i in xrange(len(data)-1)]
    g=dif[0]
    for d in dif:
        g=gcd(g,d)
    res=g-data[0]%g
    if res==g:
        return 0
    else:
        return res
        
nc=input()
for n in xrange(nc):
    data=[int(t) for t in raw_input().split()]
    data=data[1:1+data[0]]
    res=cal(data)
    print "Case #%d: %d" % (n+1, res)




