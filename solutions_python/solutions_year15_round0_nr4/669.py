n = int(input())





def alg(x,r,c): 
    if r*c % x == 0:
        if c < r:
            r,c = c,r

        if x <= 2:
            return "GABRIEL"
        
        if x == 3:
            if r == 1:
                return "RICHARD"
            else:
                return "GABRIEL"
        
        if x == 4:
            if r <= 2:
                return "RICHARD"
            else :
                return "GABRIEL"
                
        
            

    else:
        return "RICHARD"
        





for i in range(n):
    x,r,c = [int(x) for x in input().split()]
    print("Case #",i+1,": ",alg(x,r,c),sep="")

