import sys
t = input()
i = 1
while(t):
    a  = input()
    n= 4
    al= []
    while(n):
        al.append(map(int, sys.stdin.readline().split(" ")))
        n-=1
        
    b  = input()
    n = 4
    bl= []
    while(n):
        bl.append(map(int, sys.stdin.readline().split(" ")))
        n-=1
        
    intersec = set(al[a-1]).intersection(set(bl[b-1]))
    if len(intersec) == 1:
        print "Case #{}: {}".format(i,intersec.pop())
    elif len(intersec) == 0:
        print "Case #{}: Volunteer cheated!".format(i)
    else:
        print "Case #{}: Bad magician!".format(i)
    i+=1
    t-=1
