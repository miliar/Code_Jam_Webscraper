def subsetsum(array,g):

    if g == 0 or g < 1:
        return False
    elif len(array) == 0:
        return False
    else:
        if array[0] == g :
            return True
        else:
            return subsetsum(array[1:],(g - array[0])) or subsetsum(array[1:],g)


t = int(raw_input())
for tt in xrange(t) :
    c,d,v = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    
    if c == 1 :
        for r in range(1,v+1) :
            if not subsetsum(a,r) :
                a.append(r)
                
    ans = len(a) - d
    print "Case #" + str(tt+1) + ": " + str(ans)