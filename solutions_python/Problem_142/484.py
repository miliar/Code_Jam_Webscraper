import re

def cnt(s):
    ss = []
    c = s[0]
    cc = 1
    for j in range(1,len(s)):
        if s[j] == c: cc += 1
        else:
            ss.append((c, cc))
            c = s[j]
            cc = 1
    ss.append((c, cc))
    return ss

for tt in range(int(input())):
    n = int(input())
    l = [input().strip() for i in range(n)]
    
    a, b = l
    aa = re.sub(r"(.)\1+",r"\1",a)
    bb = re.sub(r"(.)\1+",r"\1",b)
    if aa == bb:
        a2 = cnt(a)
        b2 = cnt(b)
#          print (a, a2, b, b2)
        assert len(a2) == len(b2)
        r = 0
        for (i,c),(j,d) in zip(a2,b2):
            r += abs(c-d)

        print("Case #{}: {}".format(tt+1, r))
    else:
        print("Case #{}: {}".format(tt+1, "Fegla Won"))
