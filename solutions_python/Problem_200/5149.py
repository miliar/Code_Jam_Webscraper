def changeDigit(x):
    x = int(x)
    if x > 1:   return str(x-1)
    else:   return '9'

def isTidy(x):
    x = str(x)
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
    return True

def findTidy(x):
    s = str(x)
    l = len(s)
    L = list(s)
    #print(L)
    pnt = 0
    state = False
    for i in range(l-1):
        if L[i] > L[i+1]:
            state = True
            pnt = i

            for j in range(pnt,-1,-1):
                #print(j)
                if L[j] == L[pnt]:
                    pnt = j
                else:
                    break
            
            L[pnt] = changeDigit(L[pnt])
            #print(pnt)
                
            if L[i] == '9':
                L.pop()
                l -= 1
            break
        
    if state:
        for i in range(pnt+1,l):
            L[i] = '9'
    #print(L)
    return int(''.join(L))

def findTidy2(x):
    while not isTidy(x):    x -= 1
    return x

f = open('tiny-output.txt','w')
T = int(input())
for u in range(1,T+1):
    x = int(input())
    y = findTidy2(x)
    #print('Case #' + str(u),x)
    '''
    while not isTidy(x):
        x = findTidy(x)
    if x != y:
        print('not eq',x,y)
    '''
    #print('Case #' + str(u) + ': ' + str(x))
    f.write('Case #' + str(u) + ': ' + str(y) + '\n')
f.close()

    
