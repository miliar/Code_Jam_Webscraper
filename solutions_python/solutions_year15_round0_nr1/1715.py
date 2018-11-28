'''
Created on Apr 11, 2015

@author: szalivako
'''

t = int(raw_input())
for i in range(t):
    n, s = raw_input().split()
    n = int(n)
    
    for j in range(10000):
        cnt = j
        ok = True
        t = 0
        for si in s:
            x = int(si)
            if (cnt >= t):
                cnt += x
            else:
                ok = False
                break
            t += 1
            
        if (ok):
            print 'Case #' + str(i + 1) + ': ' + str(j)
            break
        
    
    '''
    cnt = 0
    j = 0
    for si in s:
        x = int(si)
        if (cnt >= j):
            cnt += x
        j += 1

    
    more = 0
    j = 0
    for si in s:
        x = int(si)
        if (cnt < j):
            more += (j - cnt)
            cnt = j + x
        j += 1
    
    print 'Case #' + str(i + 1) + ': ' + str(more)
    '''