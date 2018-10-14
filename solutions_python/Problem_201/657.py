import sys
f = open('C-large.in') 
#f = sys.stdin
#sys.stdout = open('A-small-practice.out', 'w')   

#f = open('A-large-practice.in') #sys.stdin
#sys.stdout = open('C-small.out', 'w')   
g = open('C-large.out', 'w')   

T = int(f.readline().strip())


for k in range(T):
    #print(k)
    N, K = map(int, f.readline().strip().split())
    #print(N, K)
    
    pw = 1
    K_max = 1
    while K_max <= K:
        K_max *= 2
    K_max = K_max // 2 
    #print("K_max", K_max)
    
    if K_max > 0:
        min_block = (N - K_max + 1) // K_max
        max_block = min_block + 1
        n_max_block = (N - K_max + 1) - K_max * min_block
        n_min_block = K_max - n_max_block
        #print(min_block, max_block, n_min_block, n_max_block)
         
        dK = K - (K_max - 1)
        
        if dK > n_max_block or n_max_block == 0:
            n_use = min_block
        else:
            n_use = max_block
    else:
        n_use = N    
    
    tn1 = (n_use - 1) // 2 
    tn2 = n_use - 1 - tn1
    #print(n_use, tn1, tn2)
                
    print('Case #' + str(k+1) + ': ' + str(tn2) + ' ' + str(tn1), file=g)
        
f.close()   
g.close()  



