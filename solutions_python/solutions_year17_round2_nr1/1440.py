n=int(input())
for x in range(n):
    d,nh=list(map(int,input().split()))
    oh=[]
    max=0
    for y in range(nh):
        oh.append(list(map(int,input().split())))
        oh[y].append((d-oh[y][0])/oh[y][1])
        if oh[y][2]>max:
            max=oh[y][2]
    print(r'CASE #'+str(x+1)+': '+'{0:.6f}'.format(d/max))
