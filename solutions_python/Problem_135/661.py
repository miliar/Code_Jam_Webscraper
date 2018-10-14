'''
Created on Apr 12, 2014

@author: szalivako
'''

def crossing(a, b):
    res = []
    for ai in a:
        for bi in b:
            if (ai == bi):
                res.append(ai)
    return res
                

t = int(raw_input())
cnt = 0
for i in range(t):
    r1 = int(raw_input())
    a1 = []
    for j in range(4):
        x = [int(ai) for ai in raw_input().split()]        
        a1.append(x)
    
    r2 = int(raw_input())
    a2 = []
    for j in range(4):
        x = [int(ai) for ai in raw_input().split()]
        a2.append(x)
    
    cnt += 1
    
    res = crossing(a1[r1 - 1], a2[r2 - 1])
    #print a1[r1 - 1]
    #print a2[r2 - 1]
    #print crossing(a1[r1 - 1], a2[r2 - 1])
    if (len(res) == 1):
        print 'Case #' + str(cnt) + ": " + str(res[0])
    elif (len(res) > 1):
        print 'Case #' + str(cnt) + ": Bad magician!"
    else:
        print 'Case #' + str(cnt) + ": Volunteer cheated!"
    
    