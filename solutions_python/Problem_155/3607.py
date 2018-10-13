t = int(input())
for _ in range(t):
    range1,ar = input().split()
    range1 = int(range1)
    arList = []
    for a in ar:
        arList.append(int(a))
    total = arList[0]
    add = 0
    if(total == 0):
        i = 0
        while(arList[i] == 0):
            i+=1
        add += i
        total += add
    else:
        arList[0]=0
    i = 0
    while(i<=range1):
        if(arList[i] == 0):
            i += 1
            continue
        elif(total < i):
            add += (i-total)
            total += arList[i] + (i-total)
            arList[i]=0
        else:
            total += arList[i]
            arList[i] = 0
        i += 1
    print("Case #"+str((_+1))+":",add)
