T = int(input())
for x in range(T):
    A,B,K = [int(n) for n in input().split(' ')]
    listA=[]
    for a in range(A):
        for b in range(B):
            listA.append((a,b))
    poss = 0
    for a in listA:
        p = a[0] & a[1]
        if p < K:
            poss+=1
    print('Case #' + str(x+1) + ': ' + str(poss))