
T = input() 

def fill(X, R, C): 
    if X == 1: 
        return True
    if X == 2: 
        return R*C % 2 == 0
    if X == 3: 
        return R*C % 3 == 0 and R > 1
    if X == 4: 
        if R*C % 4 != 0: 
            return False
        if R < 3 or C < 4: 
            return False
        if R >= 3: 
            return True

for t in range(T): 
    X, R, C = map(int, raw_input().split()) 
    R, C = sorted([R, C]) 

    print 'Case #%d:' %(t+1),  

    if fill(X, R, C): 
        print 'GABRIEL' 
    else: 
        print 'RICHARD' 
