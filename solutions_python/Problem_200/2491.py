def isTidy(n):
    a = list(str(n))
    for i in range(len(a) -1):
        if a[i] > a[i+1]:
            return 0
    return 1

def max_tidy_num(n):
    if isTidy(n):
        return n
    t = n
    p = 1
    for i in range(1,len(str(n))):
        s = t % 100
        if(s == 0):
            n -= p
        else:
            # while(not isTidy(s)):
            #     s -= 1
            #     n -= p
            #     st = 1
            if (not isTidy(s)):
                r = p * 10
                n = (n // r) * r - 1 
            
        p = p * 10 #decimal place to be added
        
        t = n // p
    return n





t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = int(input())
    res = max_tidy_num(s)
    print("Case #{}: {}".format(i, res))
