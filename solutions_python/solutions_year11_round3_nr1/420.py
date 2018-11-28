#!/usr/bin/python
#gcj 2011 roundC pa
T = int (input())
for cases in range(T):

    s = raw_input().split(' ')
    n = int(s[0])
    m = int(s[1])

    table = []
    for i in range(n):
        table += [raw_input()]

    done = 1
    for j in range(m):
        for i in range(n):
        
#            print str(i) + ' ' + str(j)
#            print table[i][j]
            
            if table[i][j] == '#':
                if i+1<n and j+1<m :
                    if table[i+1][j]=='#' and table[i][j+1]=='#' and table[i+1][j+1] =='#':
                        table[i] = table[i].replace('#','/',1) 
                        table[i+1] = table[i+1].replace('#','\\',1)
                        table[i] = table[i].replace('#','\\',1)
                        table[i+1] = table[i+1].replace('#','/',1)
                else :
                    done = 0
    print 'Case #'+str(cases+1)+':' 

    if done == 1:
        for i in range(n):
            print table[i]
    else:
        print 'Impossible'

