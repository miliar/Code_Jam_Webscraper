t = int(raw_input(''))
for j in range(t):
    tc = raw_input('')
    tc = list(tc)
    n = len(tc)
    for i in range(n):
        tc[i] = int(tc[i])
    for i in range(n-1):
        if tc[i] > tc[i+1]:
            i1 = i
            for k in range(i1-1,-1,-1):
                if tc[k]== tc[i]:
                    i = k 
            tc[i] = tc[i] - 1
            for k in range(i+1,n):
                tc[k] = 9
            break
    for i in range(n):
        tc[i] = str(tc[i])
    tc = ''.join(tc)
    print 'Case #' + str(j+1) + ': ' + str(int(tc))
    
    
                