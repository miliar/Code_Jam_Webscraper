def solve(d, n, horses) :
    #print(d,n,horses)
    times = []
    for i in range(0,n) :
        times += [(d - horses[i][0])/horses[i][1]]
    #print(times)
    return d/max(times)

in_t = int(input())
for i in range(0, in_t) :
    #read input
    d,n = list(map(int,input().split()))
    horses = []
    for j in range(0, n) :
        horses += [list(map(int,input().split()))]
    result = solve(d, n, horses)

    print("Case #", i+1, ": ", result, sep='')
