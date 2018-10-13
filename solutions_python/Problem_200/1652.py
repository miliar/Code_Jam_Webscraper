t=int(input())
for c in range(1,t+1):
    n=int(input())
    last = n%10
    i = 1
    m = n//pow(10,i)
    while m != 0 :
        if m%10 >last :
            n = m * pow(10,i) - 1
            last = m%10 - 1
        else:
            last = m%10
        i += 1
        m = n//pow(10,i)
    print('Case #{0}: {1}'.format(c, n))
