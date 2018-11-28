t = int(raw_input())
for i in range(1, t+1):
    n = int(raw_input())
    while n > 0:
        m = str(n)
        list = []
        for j in m:
            list.append(j)
        if list == sorted(list):
            break
        n = n - 1
    print 'Case #%d: %d' %(i, n)    
        
