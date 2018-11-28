import math
def pan(l,n,k1):
    #print l,n,k1
    p = [0 for lll in range(n)]
    k = [a for a in l]
    k = sorted(k, key = lambda x: 2*math.pi*x[0]*x[1])
    k.reverse()
    for i in range(n):
        x1 = l[i]
        count = 1
        area = math.pi*x1[0]*x1[0]+ 2*math.pi*x1[0]*x1[1]
        curr = 0
        for o in k:
            if 2*math.pi*o[0]*o[1]== 2*math.pi*x1[0]*x1[1] and curr == 0:
                curr = 1
            else:
                if count == k1:
                    break
                if o[0]<=x1[0]:
                    area += 2*math.pi*o[0]*o[1]
                    count += 1
                if count == k1:
                    break
        if count == k1:
            p[i] = area
    return max(p)

f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-small-attempt1.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    m = f[line].split()
    n,k = int(m[0]), int(m[1])
    line += 1
    l = []
    for w in range(n):
        l.append(map(int,f[line].split()))
        line += 1
    ans = pan(l,n,k)
    out.write("Case #"+str(j)+": "+str.format('{0:.40f}', ans)  + "\n")
    #print "case #"+str(j)+": "+ str.format('{0:.40f}', ans) + "\n"
out.close()