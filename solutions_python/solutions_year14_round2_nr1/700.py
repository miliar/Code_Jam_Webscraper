'''
Created on May 4, 2014

@author: szalivako
'''

T = int(raw_input())
for ti in range(T):
    n = int(raw_input())
    s1 = list(raw_input())
    s2 = list(raw_input())
    
    i = 0
    j = 0
    
    flag = True
    ans = 0
    
    while (True):
        
        #print s1[i], s2[j]
        
        if (s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            if (i == 0 and j == 0):
                flag = False
                break
            elif(s1[i] == s2[j - 1]):
                i += 1
            elif(s1[i - 1] == s2[j]):
                j += 1
            else:
                flag = False
                break
            ans += 1
            #print '+'
        if (i == len(s1) and j == len(s2)):
            break
        elif (i == len(s1)):
            if (s1[i - 1] != s2[j]):
                flag = False
                break
            else:
                i -= 1
                ans += 1
        elif (j == len(s2)):
            if (s2[j - 1] != s1[i]):
                flag = False
                break
            else:
                j -= 1
                ans += 1
        
    if (flag):
        print 'Case #' + str(ti + 1) + ': ' + str(ans)
    else:
        print 'Case #' + str(ti + 1) + ': ' + 'Fegla Won'
                
                