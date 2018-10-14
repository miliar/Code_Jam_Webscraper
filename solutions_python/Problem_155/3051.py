__author__ = 'anh'
import sys

test = sys.stdin.readline()
for num in range(int(test)+1):
    inp = sys.stdin.readline()
    (s,k) = inp.split(' ')
    res = 0
    total = 0
    for c in range(int(s)+1):
        #print(total,int(k[c]),c, res)
        if total < c:
            bonus = c - total
            total += int(k[c])+ bonus
            res += bonus
        else:
            total += int(k[c])
    print("Case #"+str(num+1)+": "+str(res))