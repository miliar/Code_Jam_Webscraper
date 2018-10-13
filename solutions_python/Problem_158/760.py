# Code Jam 2015
# Contestant: Rincewind
# Qualification Round D: Ominous Omino

def solve(x,r,c):
    if r*c % x > 0 or (x > r and x > c):
        return "Richard"
    elif x == 1 or x == 2:
        return "Gabriel"
    elif x == 3:
        return "Gabriel" if max(r,c) >= 3 and min(r,c) >= 2 else "Richard" 
    elif x == 4:
        return "Gabriel" if min(r,c) >= 3 else "Richard"

def omino():
    t = input()
    f = open('output.txt','w')
    for z in xrange(t):
        x,r,c = map(int,raw_input().split())
        print "Case #%i: %s" % (z+1,solve(x,r,c))
        f.write("Case #%i: %s\n" % (z+1,solve(x,r,c)))
omino()
