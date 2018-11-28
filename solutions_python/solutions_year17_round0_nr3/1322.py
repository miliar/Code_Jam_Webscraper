def stall(n, k):
    x = 0
    lst = [0,n+1]
    for i in range(k):
        dis = [lst[j+1]-lst[j] for j in range(len(lst)-1)]
        mn = max(dis)
        x = mn/2 + lst[dis.index(mn)]
        lst.append(x)
        lst.sort()
    left = x - lst[lst.index(x)-1]
    right = lst[lst.index(x)+1] - x
    return [left-1,right-1]

x = int(raw_input())
for j in range(x):
    [a,b] = raw_input().split(' ')
    sol = stall(int(a),int(b))
    print "Case #"+str(j+1)+": "+str(max(sol))+" "+str(min(sol))
