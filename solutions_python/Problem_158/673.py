

p1 = "RICHARD"
p2 = "GABRIEL"
def winner(x,r,c):
    global p1,p2
    if x == 1: return p2
    if x >= 7: return p1
    if (r * c) % x != 0: return p1
    if r < x and c < x: return p1
    if x > 2 and (r == 1 or c == 1): return p1
    a,b = (min(r,c),max(r,c))

    if x == 4 and a == 2: return p1 

    return p2
    

t = int(raw_input())

for i in range(0,t):
    [X,R,C] = map(int,raw_input().split(" "))
    

    print "Case #%d: %s" %(i+1,winner(X,R,C))
