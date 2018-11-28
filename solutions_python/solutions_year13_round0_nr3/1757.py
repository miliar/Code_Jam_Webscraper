import math

def check_fair(s):
    for i in range(0,len(s)/2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

n=int(raw_input())
for i in range(0,n):
    count=0;
    s=raw_input()
    l=s.split(' ')
    for j in xrange(int(l[0]),int(l[1])+1):
        if check_fair(str(j)):
            halfj = int(math.sqrt(j))
            if halfj*halfj==j:
                if check_fair(str(halfj)):
                    count+=1
    print(("Case #%d: %d" % ((i+1), count)))
