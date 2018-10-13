import os
w = raw_input()
t , q= int(w) , 0
end = []
while q < t :
    W = [int(var) for var in raw_input().split()]
    n , s , p = W[:3]
    values = W[3:]
    p_limit = 3*p
    p_1 = max(3*p - 2 , bool(p_limit)*1)
    p_2 = max(3*p - 4 , bool(p_limit)*2)
    het = s
    eg = 0
    for f in values : 
        if f >= p_1 : 
            eg += 1
        elif f >= p_2 and het > 0 :
            eg += 1 
            het -= 1
    end.append(eg)
    q += 1

p = 1
for o in end :
    print 'Case #{1}: {2}'.format('',p,o)
    p = p+1
    
print

