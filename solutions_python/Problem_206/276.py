t = int(input())

for i in range(t):
    d,n = [int(x) for x in input().split(" ")]
    hs = []
    maxtime = -1
    for j in range(n):
        hs.append([int(x) for x in input().split(" ")])
        a ,b = hs[-1]
        if maxtime < (d - a)/b:
            maxtime = (d - a)/b
    print("Case #" + str(i+1) + ": "+str(d/maxtime))
