def tatiana(n):
    n = str(n)
    if len(n)<=1:
        return n
    else:
        l = list(n)
        for i in range(2, len(n)+1):
            if l[-i]>l[-i+1]:
                l[-i] = chr(ord(l[-i])-1)
                for j in range(1, i):
                    l[-j]='9'
        if l[0] == '0':
            l = l[1:len(l)]
        return "".join(l)

t = int(raw_input())
for i in xrange(1, t + 1):
    s = tatiana(raw_input())
    print "Case #{}: {}".format(i, s)
