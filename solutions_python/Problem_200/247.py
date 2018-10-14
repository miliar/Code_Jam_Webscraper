T = int(input())
for case in range(T):
    N = list(int(i) for i in input())
    
    for i in range(len(N)-1,0,-1):
        if (N[i-1]) > (N[i]):
            for j in range(i,len(N)):
                N[j] = 9
            N[i-1] -= 1
            
    while N[0] == 0:
        del N[0]
    
    num = "".join(str(x) for x in N)
    #print(S)
    outstr = "Case #{}: ".format(case+1)
    print(outstr + num)
    