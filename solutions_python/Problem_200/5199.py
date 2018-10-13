def fun(n):
    m = str(n)
    count = 0
    k = 0
    while k < len(m)-1:
        if m[k] > m[k+1]:
            count += 1
            break
        k = k + 1
    if count == 0:
        return True
    else:
        return False
        
t = int(input())
for i in range(t):
    n = int(input())
    while n > 0:
        if fun(n):
            print("Case #"+str(i+1)+": "+str(n))
            break
        else:
            n = n - 1
