def is_good (s,a,b):
    if s[0]!=0 and int(s) >=a and int(s) <= b:
        return True
    return False

t = int(raw_input())
for i in range(1,t+1):
    line = raw_input().split()
    a = int(line[0])
    b = int(line[1])
    pairs = 0 
    for j in range(a,b+1):
        s = str(j)
        rots = set()
        for k in range(0,len(s)):
            if is_good(s[k:]+s[:k],a,b):
                rots.add(s[k:]+s[:k])
        pairs += len(rots)-1
    print "Case #{}: {}".format(i,pairs//2)
