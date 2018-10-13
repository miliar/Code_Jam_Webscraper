t = int(input())            

for test in range(t):
    d, n = map(int, input().split())
    horses = []
    for i in range(n):
        k,s = map(int, input().split())
        horses.append((k,s))
    ans = 10**18
    for horse in horses:
        temp = (d - horse[0])/horse[1]
        temp = d / temp
        ans = min(ans, temp)
    print("Case #"+str(test + 1)+": "+str(ans))
