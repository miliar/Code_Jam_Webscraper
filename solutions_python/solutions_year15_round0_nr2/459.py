T = int(input())

for CC in range(T):
    D = int(input())
    P = list(map(int,input().split()))
    P.sort(reverse=True)

    #print(P)

    Ans = []
    Cnt = 0
    for x in range(P[0],0,-1):
        Ans.append(x+sum([(y-1)//x for y in P]))
        Cnt += 1
        #print(Cnt-1,Ans[-1])
        
    print('Case #{}: {}'.format(CC+1,min(Ans)))
