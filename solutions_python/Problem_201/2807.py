from __future__ import division
import bisect 
def f(n, k):
    #s = [0] * (n+2)
    s = [0, n+1]
    ls = 0
    rs = 0
    for _ in xrange(k):
        oldcenter = [0, 0]
        for i in xrange(len(s)-1):
            mid = (s[i+1] - s[i]) / 2
            if s[i+1] == s[i]:
                continue
            if (s[i+1] - s[i]) % 2 == 0:
                center = (s[i+1] + s[i]) // 2
                dist = mid
                if dist > oldcenter[1]:
                    oldcenter[1] = dist
                    oldcenter[0] = center
                    ls = center - s[i] - 1
                    rs = s[i+1] - center - 1
                #print "a"
                #print "c", center
            else:
                center1 = (s[i+1] + s[i]) // 2
                center2 = center1 + 1
                dist = mid
                if mid > oldcenter[1]:
                    oldcenter[1] = dist
                    oldcenter[0] = center1
                    ls = center1 - s[i] - 1
                    rs = s[i+1] - center1 - 1
                #print "b"
                #print "c1", center1
            if s[i] == -1:
                print ls
                print rs
                print center1
                print "s", s[i], s[i+1]
                print mid
                print s
                print oldcenter
            
        bisect.insort(s, oldcenter[0])
        #print oldcenter[0]
    #print s
    #print oldcenter[0]
    return rs, ls

with open("output3-3.txt", 'w') as f2:
    with open("C-small-1-attempt2.in", 'r') as f1:
    #with open("in3.txt", 'r') as f1:
        f1.readline()
        for i, line in enumerate(f1):
            
            g = line.strip().split(' ')
            x1, x2 = int(g[0]), int(g[1])
            #if x2 > x1 // 2:
            #    continue
            val = f(x1, x2)
            f2.write("Case #{}: {} {}\n".format(i+1, int(val[0]), int(val[1])))
            
#print f(5,2)