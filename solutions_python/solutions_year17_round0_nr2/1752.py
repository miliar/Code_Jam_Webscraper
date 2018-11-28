# tidy numbers
# code jam - qualification round - 2017
# uses python 3

T = int(input().strip())    # number of cases
for t in range(1,T+1):
    
    N = [int(c) for c in input().strip()][::-1]

    last_i = 0
    for i in range(1,len(N)):
        if N[i]>N[i-1]:
            for j in range(last_i,i):
                N[j] = 9
            if ((i==len(N)-1) and N[i]==1):
                N.pop()
            else:
                N[i] -= 1
            last_i = i    

    ans = ''.join(map(str,N[::-1]))        

                        
    print('Case #{}: {}'.format(t, ans))    