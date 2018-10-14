import math
def tidy(n):
    if (n < 10):
        return n   
    isTidy = False
    digits = int(math.log10(n))+1
    special = False
    ones = True
    cnt = 0
    for k in range(digits - 1,-1,-1):
        dig = (n // 10**k) % 10
        if (dig != 1 and cnt <= 1):
            ones = False
        elif (ones and dig == 1):
            cnt += 1
    while (not isTidy):
        last = 10
        i = 0
        while(i < digits):
            dig = (n // 10**i) % 10
            if (dig > last):
                if (ones and (i < cnt)):
                    n = n - 10**i                    
                    n = n - last*(10**(i-1))
                    n = n + 9*(10**(i-1))
                elif (ones):
                    n = n - 10**i  
                    for j in range(0,i):
                        n = n + 9*(10**(j))
                else:
                    n = n - (last + 1)
                i = digits
            elif(i == digits - 1):
                isTidy = True
                i += 1
            else:
                last = dig
                i += 1
                
    return n
                          

t = int(input())
for i in range(1, t + 1):
    inputS = input().split(" ")
    n = int(inputS[0]) 
    print("Case #{}: {}".format(i, tidy(n)))

