def check(N,K,kList,c):

    p = [0 for _ in range(K)]
    
    ## test all possibilities for products
    for i in range(2**N):
        prod = 1
        for bit in range(N):
            if ((i>>bit)&1)==1:
                prod *= c[bit]
        for k in range(K):
            if prod == kList[k]:
                p[k] += 1

    
    ## if one product is not possible, return score 0
    for item in p:
        if item==0:
            return 0

    ## simple approach: return total matches
    return sum(p)
            
    

def solve(R,N,M,K,kList):
    
    ## test all possibilities
    c = [2 for _ in range(N)]
    cRes = c
    bestGuess = 0

    while True:

        ## evaluate possibility
        r = check(N,K,kList,c)
        if r>bestGuess:
            bestGuess = r
            cRes = list(c)

        ## next
        digit = 0
        while digit<N:
            c[digit] += 1
            if c[digit]>M:
                c[digit]=2
                digit += 1
            else:
                break
        if digit==N:
            break
        
    s = ''
    for card in cRes:
        s=s+str(card)
    return s
                    
##            
## MAIN PROGRAM
##
T = int(input())
for t in range(T):
    ## read case
    R,N,M,K = map(int, input().rstrip().split())
    k = [list(map(int, input().rstrip().split())) for _ in range(R)]
        
    ## solve and print result
    print('Case #'+str(t+1)+':')
    for item in k:
        result = solve(R,N,M,K,item)
        print(str(result))


    
