'''
Created on Apr 12, 2014

@author: szalivako
'''

t = int(raw_input())
for k in range(t):
    n = int(raw_input())

    a = [ai for ai in raw_input().split()]
    b = [bi for bi in raw_input().split()]
    
    a.sort()
    b.sort()
    
    #print av
    #print b
    
    sum1 = 0
    i = 0
    j = 0
    while (j < n):
        if (a[i] < b[j]):
            i += 1
            j += 1
        else:
            j += 1
            sum1 += 1
    
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    #print a
    #print b
    
    sum2 = 0
    i = 0
    j = 0
    while (j < n):
        if (a[i] > b[j]):
            i += 1
            j += 1
        else:
            j += 1
            sum2 += 1
    sum2 = n - sum2
    
    print 'Case #' + str(k + 1) + ": " + str(sum2) + ' ' + str(sum1)