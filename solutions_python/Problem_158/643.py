def winner(X,R,C):
    return ["RICHARD", "GABRIEL"][_winner(X,R,C)]
    
def _winner(X,R,C):
    if X == 1:
        return 1
    if X == 2:
        return 1 if (R*C)%2 == 0 else 0
        
    k = tuple(sorted((R,C)))
    if X == 3:
        return {(1,1):0,
                (1,2):0,
                (1,3):0,
                (1,4):0,

                (2,2):0,
                (2,3):1,
                (2,4):0,

                (3,3):1,
                (3,4):1,
                
                (4,4):0}[k]

    if X == 4:
        return {(1,1):0,
                (1,2):0,
                (1,3):0,
                (1,4):0,

                (2,2):0,
                (2,3):0,
                (2,4):0,

                (3,3):0,
                (3,4):1,

                (4,4):1}[k]
                
if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1,T+1):
        X,R,C = map(int, raw_input().split())
        print "Case #%d: %s" % (i, winner(X,R,C))
