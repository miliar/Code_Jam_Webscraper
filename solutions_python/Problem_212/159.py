T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split(" "))
    G = list(map(int, input().split(" ")))

    ans = 0
    i = 0
    while i < len(G):
        if G[i]%P == 0:
            del G[i]
            ans += 1
        else:
            i += 1
    
    if P == 2:
        ans += int((len(G)+1)/2)
    if P == 3:
        mod1 = len([n for n in G if n%P == 1])
        mod2 = len([n for n in G if n%P == 2])
        minV = min(mod1, mod2)
        remV = max(mod1, mod2) - minV
        ans += minV
        ans += int((remV+2)/3)
    if P == 4:
        mod1 = len([n for n in G if n%P == 1])
        mod2 = len([n for n in G if n%P == 2])
        mod3 = len([n for n in G if n%P == 3])
        min13 = min(mod1, mod3)
        rem13 = max(mod1, mod3) - min13
        rem2 = 1 if mod2%2 == 1 else 0
        ans += min13
        ans += int(mod2/2)
        if rem2 == 1:
            if rem13 >= 2:
                ans += 1
                rem13 -= 2
            else:
                ans += 1
                rem13 = 0
        ans += int((rem13+3)/4)

    
    print("Case #{}: {}".format(t, ans))