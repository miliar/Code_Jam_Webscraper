T = int(input())

for CC in range(T):
    Smax, Ss = input().split()
    Smax = int(Smax)

    nowstand, Ans = 0, 0

    for x in range(len(Ss)):
        if x <= nowstand:
            nowstand += int(Ss[x])        
        else:
            Ans += x-nowstand
            nowstand = x+ int(Ss[x])

    print('Case #{}: {}'.format(CC+1,Ans))
