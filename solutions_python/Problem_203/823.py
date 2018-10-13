from copy import deepcopy
dc = deepcopy

for xyz in range(1,int(input())+1):
    n,m = map(int,input().split())
    a = []
    a.append(['?']*(m+2))

    for _ in range(n):
        b = ['?']
        b.extend(list(input()))
        b.append('?')
        a.append(b)

    a.append(['?']*(m+2))

    c = {}
    orig = dc(a)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j] == '?':
                continue
            try:
                c[a[i][j]] += 1
            except:
                c[a[i][j]] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j] == '?':
                continue
            if c[a[i][j]] > 1 and orig[i][j] != '?':
                for k in range(i,n+1):
                    for l in range(1,m+1):
                        if a[k][l] == a[i][j]:
                            for o in range(min(i,k),max(i,k)+1):
                                for p in range(min(j,l),max(j,l)+1):
                                    a[o][p] = a[i][j]
                                    
    b = {}
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j] in b or a[i][j] == '?':
                continue
            l = i
            r = i
            l1 = j
            r1 = j
            for k in range(i+1,n+1):
                if a[k][j] == a[i][j]:
                    r = k
                else:
                    break
            for k in range(j+1,m+1):
                if a[i][k] == a[i][j]:
                    r1 = k
                else:
                    break
            b[a[i][j]] = (l,r,l1,r1)   
  
    for k in b:
        l = b[k][0]
        r = b[k][1]
        l1 = b[k][2]
        r1 = b[k][3]
        for j in range(b[k][2]-1,0,-1):
            check = True
            for i in range(l,r+1):
                if a[i][j] != '?':
                    check = False
                    break
            if not check:
                break
            for i in range(l,r+1):
                a[i][j] = k
            l1 -= 1
            
        for j in range(b[k][3]+1,m+1):
            check = True
            for i in range(l,r+1):
                if a[i][j] != '?':
                    check = False
                    break
            if not check:
                break
            for i in range(l,r+1):
                a[i][j] = k
            r1 += 1   
        
        b[k] = (l,r,l1,r1)    
    
    for k in b:
        l = b[k][0]
        r = b[k][1]
        l1 = b[k][2]
        r1 = b[k][3]
        for i in range(b[k][0]-1,0,-1):
            check = True
            for j in range(l1,r1+1):
                if a[i][j] != '?':
                    check = False
                    break
            if not check:
                break
            for j in range(l1,r1+1):
                a[i][j] = k
            l -= 1
            
        for i in range(b[k][1]+1,n+1):
            check = True
            for j in range(l1,r1+1):
                if a[i][j] != '?':
                    check = False
                    break
            if not check:
                break
            for j in range(l1,r1+1):
                a[i][j] = k
            r += 1    
        
        b[k] = (l,r,l1,r1)
    

    while True:
        change = False
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[i][j] == '?':
                    pass
        if not change:
            break


    print("Case #"+str(xyz)+': ')
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(a[i][j],end='')
        print() 