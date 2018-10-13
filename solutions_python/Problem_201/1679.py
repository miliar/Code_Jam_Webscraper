# bathroom stalls
# code jam - qualification round - 2017
# uses python 3
import math

T = int(input().strip())    # number of cases
for t in range(1,T+1):
    
    N, K = [int(v) for v in input().strip().split()]

    d = 2**(int(math.log(K,2))+1)
    z = max(0, N-(d-1))//d
    p = min(N, (z*d+(d-1)))
    k0 = (d//2) - 1
    k1 = (d) - 1
    diff = N-p
    full_add = max(0, diff - (k1-k0))
    half_add = max(0, diff - (full_add*2))
    min_val = z
    max_val = z
    if K-k0<=(half_add+full_add):
    	max_val += 1
    if K-k0<=full_add:	
    	min_val += 1 	      
    	

    print('Case #{}: {} {}'.format(t, max_val, min_val))    