repeat = int(input())
for t in range(repeat):
    n, x=(int(a) for a in input().split(" "))
    s=[]
    table=[]
    for i in range(701):
        table.append(0)
    s=[int(a) for a in input().split(" ")]
    for a in s:
        table[a] += 1
    s.sort()
    result=0
    nleft=n
    for i in range(n):
        if nleft == 0:
            break
        target = s[i]
        if table[target] == 0:
            continue
        table[target] -=1
        start = x-target
        for j in range(start,0,-1):
            if table[j] != 0:
                table[j] -= 1
                nleft -= 1
                break
        nleft -= 1
        result+=1
    print("Case #"+str(t+1)+": "+str(result))