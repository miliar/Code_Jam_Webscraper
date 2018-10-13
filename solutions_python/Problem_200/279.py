def toint(L): return int(''.join(map(str, L)))
T = input()
for t in range(1, T+1):
    print 'Case #%d:' % t,
    N = map(int,raw_input())
    n = len(N)
    for i in range(1,n):
        if N[i] < N[i-1]:
            for j in range(i-1, -1, -1):
                if N[j] < N[i-1]:
                    break
            else: j -= 1
            j += 1
            print toint(N[:j] + [N[j] - 1] + [9] * (n - j - 1))
            break
    else: print toint(N)
            


                    
        
        

    

    
