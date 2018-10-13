from fractions import gcd
from functools import reduce

def readints(f):
    return [int(x.strip()) for x in f.readline().split()]

fn = "C-large"
with open(fn+".in","r") as inp:
    with open(fn+".out","w") as out:
        tests = readints(inp)[0]
        for test in range(1,tests+1):
            print("Test",test)
            r,k,n = readints(inp)
            a = readints(inp)
            b = []
            for i in range(n):
                aa = a[i:]+a[:i]
                s = 0
                for j in range(n):
                    if s+aa[j] > k:
                        b.append(((i+j)%n,s))
                        break
                    s+=aa[j]
                else:
                    b.append((i,sum(a)))
            lasttime = [-1]*n
            lastsum = [0]*n
            p = 0
            res = 0
            while r > 0:
                if lasttime[p]!=-1:
                    full = r//(lasttime[p]-r)
                    res += full*(res-lastsum[p])
                    r%=(lasttime[p]-r)
                    lasttime = [-1]*n
                else:
                    lasttime[p]=r
                    lastsum[p]=res
                    p,add = b[p]
                    res+=add
                    r-=1
            out.write("Case #{0}: {1}\n".format(test,res))
            
