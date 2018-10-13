t = int(input())

for i in range(1, t + 1):
    p, k = [s for s in raw_input().split(" ")]
    
    p = list(p_j == '+' for p_j in p)
    k = int(k)
    
    amount = 0
    ptr = 0
    
    while ptr + k <= len(p):
        if p[ptr] == False:
            p[ptr:ptr+k] = list(not p_j for p_j in p[ptr:ptr+k])
            amount += 1
            
        ptr += 1
        
    res = 'IMPOSSIBLE' if False in p else amount
    
    print("Case #{}: {}".format(i, res))