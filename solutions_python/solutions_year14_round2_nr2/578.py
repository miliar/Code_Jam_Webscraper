'''
Created on May 3, 2014

@author: szalivako
'''

T = int(raw_input())
for ti in range(T):
    a, b, k = map(int, raw_input().split())
    
    ans = 0
    for i in range(a):
        for j in range(b):
            if (i & j < k):
                ans += 1
    
    print 'Case #' + str(ti + 1) + ': ' + str(ans)
            
    