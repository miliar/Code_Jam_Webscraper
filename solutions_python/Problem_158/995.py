f = open('D-small-attempt3.in', 'r')

T = int(f.readline().strip())


for t in xrange(T):

    X, R, C = [int(x) for x in f.readline().strip().split(" ")]

    s=""
    if X==1:
        s = "GABRIEL" 
    elif X==2:
        if [R,C] in [[1,1],[1,3],[3,1],[3,3]]:
            s = "RICHARD"
        elif [R,C] in [[1,2],[1,4],[2,1],[4,1],[2,2],[2,3],[2,4],[3,2],[4,2],[3,4],[4,3],[4,4]]:
            s = "GABRIEL" 
    elif X==3:
        if [R,C] in [[2,3],[3,3],[3,4],[3,2],[4,3]]:
            s = "GABRIEL"
        elif [R,C] in [[1,1],[1,2],[1,3],[1,4],[2,2],[2,4],[4,4],[2,1],[3,1],[4,1],[4,2]]:
            s = "RICHARD" 
    elif X==4:
        if [R,C] in [[3,4],[4,3],[4,4]]:
            s = "GABRIEL"
        else:    
            s = "RICHARD"

    print 'Case #%d: %s'% (t+1,s)