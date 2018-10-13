def bfs(target, flipper):    
    init= ""
    for i in range(0, len(target)):
        init = init+'+'
    if target == init:
        return 0
    
    visited = set([init])
    cur = set([init])
    count = 0
    imp = True
    
    while True:
        imp = True
        newcur =set([])
        count += 1
        for s in cur:
            l = list(s)
            
            for i in range(0, len(target)+1 - flipper):
                temp = list(l)
                for j in range(i, i+flipper): #flip
                    if temp[j] == '+':
                        temp[j] = '-'
                    elif temp[j] == '-':
                        temp[j] = '+'
                    else:
                        print 'exception!!!!! ', temp[j]
                
                temp = ''.join(temp)
                
                if temp == target:
                    return count
                elif temp in visited:
                    pass
                else:
                    imp = False
                    newcur.add(temp)
                    visited.add(temp)
        if imp == True:
            return 'IMPOSSIBLE'
        cur = newcur
        
        
t = int(raw_input())
for i in xrange(1, t + 1):
    inputs = raw_input().split(" ")
    s = bfs(inputs[0], int(inputs[1]))
    print "Case #{}: {}".format(i, s)
