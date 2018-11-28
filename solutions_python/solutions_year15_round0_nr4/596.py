import math
cases = int(input())


def resolve(X,R,C):

    if R*C % X != 0:
        return "RICHARD"
    if X > max(R,C):
        return "RICHARD"
##    if math.floor(math.sqrt(X)) > min(R,C):
##        return "RICHARD"
    i = 0
    while i < X/2:
        if i+1 > min(R,C):
            return "RICHARD"
        i+= 1
##    if math.ceil(math.sqrt(X)) > min(R,C):
##        return "RICHARD"
    if X == 4:
        if R == 4 and C == 2 or\
               C == 4 and R == 2:
           return "RICHARD"
    
    return "GABRIEL"    


for i in range(cases):
    X,R,C = map(int,input().split())
    print("Case #"+str(i+1)+":",resolve(X,R,C))

   
