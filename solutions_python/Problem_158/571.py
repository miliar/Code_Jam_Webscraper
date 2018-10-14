

def main(filename):
    
    with open('../data/output4.txt', 'w') as g:
        with open(filename) as f:
            N = int(f.readline())
            
            for i in range(N):
                X, R, C = [int(x) for x in f.readline().split()]
                print X, R, C
                print "Case #%s: %s" % (i + 1, omni(X, R, C))
                g.write("Case #%s: %s\n" % (i + 1, omni(X, R, C)))
            
            
def omni(X, R, C):
    if X == 1:
        return "GABRIEL"
    if R == 1:
        if X >= 3:
            return "RICHARD"
        else:
            return "GABRIEL" if C % X == 0 else "RICHARD"
    if C == 1:
        if X >= 3:
            return "RICHARD"
        else:
            return "GABRIEL" if R % X == 0 else "RICHARD"
    if R == 2:
        if C == 2:
            return "RICHARD" if X >= 3 else "GABRIEL"
        if C == 3: 
            return "RICHARD" if X == 4 else "GABRIEL"
        if C == 4:
            return "RICHARD" if X == 3 or X == 4 else "GABRIEL"
    if C == 2:
        if R == 2:
            return "RICHARD" if X >= 3 else "GABRIEL"
        if R == 3: 
            return "RICHARD" if X == 4 else "GABRIEL"
        if R == 4:
            return "RICHARD" if X == 3 or X == 4 else "GABRIEL"
    if R == 3:
        if C == 3:
            return "RICHARD" if X == 2 or X == 4 else "GABRIEL"
        if C == 4:
            return "GABRIEL"
    if C == 3:
        if R == 3:
            return "RICHARD" if X == 2 or X == 4 else "GABRIEL"
        if R == 4:
            return "GABRIEL"
    if C == 4 and R == 4:
        return "RICHARD" if X == 3 else "GABRIEL"

if __name__=="__main__":
    
#     main("../data/ominotest.txt")
    main("../data/plop.txt")