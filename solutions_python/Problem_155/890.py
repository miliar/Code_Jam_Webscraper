
T = input() 

for t in range(T): 
    _, _S = raw_input().split()
    S = map(int, _S)  
    n = len(S) 

    H = list(S)
    for i in range(1, n): 
        H[i] += H[i-1]

    val = 0
    for i in range(1, n): 
        if i > H[i-1]: 
            val = max(val, i - H[i-1]) 

    print 'Case #%d:' %(t+1), val
