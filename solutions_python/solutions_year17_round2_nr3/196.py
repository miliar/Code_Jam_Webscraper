f = open('ans2.txt', 'w')
T = int(input())
for i in range(1,T+1):
    N, Q = map(int, input().split())
    t = 0
    horses = []
    dist = []
    for j in range(N):
        o, k = map(int, input().split())
        horses.append([o, k, 0])
    for l in range(N-1):
        s = list(map(int, input().split()))
        dist.append(s[l+1])
    input()
    input()
    hs = []
    hs.append(horses[0])
    for p in range(N-1):
        temp = []
        c = horses[p + 1]
        c[2] = 1000000000000000
        for horse in hs:
            horse[0]-=dist[p]
            if horse[0]>=0:
                horse[2]+=dist[p]/horse[1]
                print(horse[2])
                c[2] = min(c[2], horse[2])
                temp.append(horse)
        temp.append(c)
        hs = temp
    ans = 1000000000000000
    for horse in hs:
        ans = min(ans, horse[2])
        print(horse[2])


    f.write(f"Case #{i}: {ans}\n")