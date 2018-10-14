def makeroster(R,C):
    for x in xrange(C):
        print '#'*R
    pass
def case(X,R,C):
    if X == 1: return 'GABRIEL'
    if R*C == 2 and X == 2: return 'GABRIEL'
    if R*C < 2 * X: return 'RICHARD'
    if R*C % X != 0: return 'RICHARD'
    if X == 2 and R*C % X == 0: return 'GABRIEL'
    if R == 2:
        if C == 3:
            if X == 3: return 'GABRIEL'
        if C == 4:
            if X == 4: return 'RICHARD'
    if R == 3:
        if C == 2:
            if X == 3: return 'GABRIEL'
        if C == 3:
            if X == 3: return 'GABRIEL'
        if C == 4:
            if X == 3: return 'GABRIEL'
            if X == 4: return 'GABRIEL'
    if R == 4:
        if C == 2:
            if X == 4: return 'RICHARD'
        if C == 3:
            if X == 3: return 'GABRIEL'
            if X == 4: return 'GABRIEL'
        if C == 4:
            if X == 4: return 'GABRIEL'
def main():
    T = int(raw_input())
    for i in range(T):
        X,R,C = map(int,raw_input().split())
        #makeroster(R,C)
        #print X
        print "Case #"+str(i+1)+": "+case(X,R,C)
if __name__ == '__main__':
    main()