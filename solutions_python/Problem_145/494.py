import math
def find(P, Q):
    a = 0.5
    f = P/Q
    count = 1;
    if not isValid(P,Q):
        return 'impossible'
    while True:
        if f >= a:
            return str(count)
        else:
            a = a/2
            count = count + 1
    
def isValid(P, Q):
    a = 0.5
    f = P/Q
    for i in range(1,41):
        if (f/a == int(f/a)) :
            return True
        a=a/2
    return False

T = int(raw_input())
B = open('R1CQ1.out','w')
for i in range(1, T+1):
    P,Q = raw_input().split('/')
    P,Q = float(P),float(Q)
    print P
    print Q

    B.write("Case #" + str(i) + ": " + find(P,Q) + "\n")
B.close()
