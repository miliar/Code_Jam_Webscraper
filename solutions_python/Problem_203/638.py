t = int(input())
for i in range(1, t+1):
    print("Case #{}:".format(i))
    r, c = [int(s) for s in input().split(" ")]
    ll = []
    for j in range(r):
        l = list(input())

        for k in range(0, c-1):
            if l[k+1] == '?' and l[k] != '?':
                l[k+1] = l[k]

        for k in range(c-1, 0, -1):
            if l[k-1] == '?' and l[k] != '?':
                l[k-1] = l[k]    

        ll.append(l)

    for j in range(0, r-1):
        if ll[j+1][0] == '?' and ll[j][0] != '?':
            ll[j+1] = ll[j]
    
    for j in range(r-1, 0, -1):
        if ll[j-1][0] == '?' and ll[j][0] != '?':
            ll[j-1] = ll[j]
        

    for j in range(r):
        print("{}".format(''.join(str(e) for e in ll[j])))

