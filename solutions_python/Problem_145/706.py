import sys

def genElf(num, den, ans):
    if den & (den-1):   print "impossible"
    else:
        while num < den:
            num = num * 2
            ans = ans + 1
        print ans
    
for i in range(1,input()+1):
    p,q = map(int, raw_input().split("/"))
    print "Case #%i:" % (i),
    genElf(p,q,0)
        
