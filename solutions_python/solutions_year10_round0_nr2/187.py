from fractions import gcd
from functools import reduce

def readints(f):
    return [int(x.strip()) for x in f.readline().split()]

fn = "B-large"
with open(fn+".in","r") as inp:
    with open(fn+".out","w") as out:
        tests = readints(inp)[0]
        for test in range(1,tests+1):
            a = readints(inp)[1:]
            g = reduce(gcd, (abs(x-a[0]) for x in a))
            res = (g-a[0]%g)%g
            out.write("Case #{0}: {1}\n".format(test,res))
            
