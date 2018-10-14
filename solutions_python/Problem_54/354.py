C = int(raw_input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for case in range(1, C + 1):
    num = map(int, raw_input().split())
    N = num[0]
    num = sorted(num[1:])
    
    c = len(num) - 1
    while c > 0:
        num[c] = num[c] - num[c - 1]
        c -= 1 
        
    firstNum = num[0]
    num = num[1:]
    #print num
    
    tmp = num[0]        
    for i in range(1, len(num)):
        tmp = gcd(tmp, num[i])
        
    #print tmp 
    
    t = tmp - (firstNum % tmp)
    
    if t == tmp:
        t = 0

    print "Case #%d: %d" % (case, t)
