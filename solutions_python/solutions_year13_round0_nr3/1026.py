import math
width = 0
depth = 0

S = set(x for x in range(1,10))

def isPal(y):
    x = int(y)
    if x < 10:
        return True
    s = str(x)
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            return False
    return True
    


def solve(start, end):
    total = 0
    for i in range(start, end+1):
        sq = math.sqrt(i)
        # if i == 4:
        #    import pdb; pdb.set_trace()
        # if sq.is_integer():
           # print  
        if (not sq.is_integer()) or (sq >= start and (not sq in S)):
            continue
        elif isPal(i):
            S.add(i)
            if sq in S:
                total += 1
            elif isPal(sq):
                S.add(sq)
                total += 1
    return total



f = open('input.in', 'r')
out = open('Aoutput', 'w')
l = f.readline()
num = int(l)
for i in range(num):
    l = f.readline()
    sp = l.split()
    depth = int(sp[0])
    width = int(sp[1])
    
    # f.readline()
    # import pdb; pdb.set_trace()
    print "Case #{0}: {1}".format(i+1, solve(depth, width))