import sys
import time
from itertools import permutations, combinations

in_name = sys.stdin
out_name = sys.stdout

fin = sys.stdin
fout = sys.stdout

class inout:
    IN = fin
    
    @classmethod
    def line(cls, type=str):
        return type(cls.IN.readline().strip())
        
    @classmethod 
    def splitline(cls, type=str):
        return [type(x) for x in cls.IN.readline().split()]


T = inout.line(int)
result = []

t1 = time.time
for test in range(int(T)):
    #Read input
    nums = inout.splitline(int)[1:]
    d = {}
    isgood = False
    for i in range(19):
        if isgood:
            break
        for vals in combinations(nums, i + 1):
            s = sum(vals)
            if s in d and vals != d[s]:
                isgood = True
                s1 = ' '.join([str(el) for el in d[s]])
                s2 = ' '.join([str(el) for el in vals])                
                break
            else:
                d[s] = vals
    if isgood:
        result.append("Case #%d:\n%s\n%s\n" % (test+1,s1, s2))
    else:
        result.append("Case #%d:\nImpossible\n" % (test))
    

fout.writelines(result)
fout.close()
fin.close()
t2 = time.time
#print t2 - t1