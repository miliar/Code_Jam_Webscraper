t = int(input())

for i in range(t):
    n = int(input())
    t = t-1
    while(n):
        m = sorted(list(str(n)))
        m = int(''.join(m))
        if(n == m):
            print ('Case #' + str(i+1) + ':',n)
            break
        else:
            n = n-1;

