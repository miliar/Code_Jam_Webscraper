T = input()
for test in range(1,T+1):
    count = 0
    possible = 1
    [s, K] = raw_input().split()
    l = len(s)
    S = list(s)
    K = int(K)
    for x in range((l - (K-1))):
        if (S[x] == '-'):
            count += 1
            for y in range(x,x+K):
                if S[y]=='-':
                    S[y]='+'
                else:
                    S[y]='-'

    for x in range((l - (K-1)),l):
        if (S[x] == '-'):
            possible=0
            break
    if possible==0:
        print ('Case #'+str(test)+': IMPOSSIBLE')
    else:
        print ('Case #'+str(test)+': '+str(count))