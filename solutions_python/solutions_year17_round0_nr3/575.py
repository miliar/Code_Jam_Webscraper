import math
inf = 10**19
data = []
depth = 0

def recurse(stalls, person):

    if (stalls == person):
        return (0, 0)

    global depth
    depth += 1
    if (person == 0):
        return (inf, inf)    

    if(person == 1):
        if (stalls % 2 == 0):
            return (stalls/2, stalls/2 - 1)

        else:
            return (stalls/2, stalls/2)        

    if ((((stalls-1)/2) == stalls/2) and ((person-1)/2 == person/2)):
    	a = recurse((stalls-1)/2, (person-1)/2)
    	return a

    if (((stalls/2 - (stalls-1)/2) == 1) and (person/2 == (person-1)/2)):
        a = recurse((stalls-1)/2, (person-1)/2)
    	return a

    if ((((stalls-1)/2) == stalls/2) and (person/2 - (person-1)/2 == 1)):    
        # a = recurse((stalls-1)/2, (person-1)/2)
        # if a == (0, 0):
        #     return (0, 0)

        # else:
        #     b = recurse(stalls/2, person/2)

        # return (min(a[0], b[0]), min(a[1], b[1]))
        b = recurse(stalls/2, person/2)
        return b

    if (((stalls/2 - (stalls-1)/2) == 1) and (person/2 - (person-1)/2 == 1)):
        b = recurse(stalls/2, person/2)
        return b

    a = recurse((stalls-1)/2, (person-1)/2)
    # print "a", stalls, person
    b = recurse(stalls/2, person/2)
    # print "b", stalls, person
    return (min(a[0], b[0]), min(a[1], b[1]))

    # else:
        # recurse((stalls-1)/2)                

# inp = open("in", "r")
# out = open("ou", "w")
# inp = open("C-small-1-attempt0.in", "r")
# out = open("C-small-12-output", "w")
# inp = open("C-small-2-attempt0.in", "r")
# out = open("C-small-2-output", "w")
inp = open("C-large.in", "r")
out = open("C-large-output", "w")
tt = int(inp.readline())
for i in xrange(tt):
    s = inp.readline().split()
    n = int(s[0])
    k = int(s[1])
    ans = recurse(n, k)
    out.write("Case #%d: %d %d\n" % (i+1, ans[0], ans[1]))

inp.close()
out.close()