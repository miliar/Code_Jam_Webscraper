import sys

x = 0;
n = sys.stdin.readline()
n = int(n)



while (x < n):
    x = x + 1 #count
    num = 0
    
    rt = sys.stdin.readline().split()
    
    t = int(rt[1])
    r = int(rt[0])
    
    while ( t > 0):
        s = (2 * r) + 1
        if (t - s) >= 0 :
            num = num  + 1
        t = t - s
        r = r + 2
        
    print("Case #",x,": ",num, sep='')