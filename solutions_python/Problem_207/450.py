import operator
for _ in range(int(input())):
    n,r,o,y,g,b,v = list(map(int, input().split()))
    h = n/2
    for i in r,o,y,g,b,v:
        if i>n/2:
            print("Case #"+str(_+1)+": IMPOSSIBLE")
            h=0
            break
    if h==0:
        continue
    d = {}
    d['R'] = r
    d['Y'] = y
    d['B'] = b
    l = [None] * n
    iter = 0
    sord = sorted(d.items(), key=operator.itemgetter(1))
    for j in sord:
        for i in range(j[1]):
            l[iter] = j[0]
            iter +=2
            if(iter == n or iter>n):
                iter = 1
    print("Case #"+str(_+1)+": ",end="")
    for i in range(n):
        print(l[i],end="")
    print('')
