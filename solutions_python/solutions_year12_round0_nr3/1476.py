


def countRecycled(a, b):
    v = 0
    for m in xrange(a+1, b+1):
        for n in xrange(a, m):
            for j in xrange(len(str(n))):
                if(str(n)[j:]+str(n)[:j]) == str(m): 
                    v += 1
                    break
    return v 


if __name__=='__main__':
    f = open("P-Cinput.txt", "r")
    outsies = open("P-Coutput.txt", "w")
    lines = f.readlines()
    t = int(lines[0].rstrip())
    for i in xrange(t):
        line = [int(x) for x in lines[i+1].rstrip().split()]
        a, b = line[0], line[1]
        v = countRecycled(a, b)
        outsies.write("Case #{0}: {1}\n".format(i+1, v))

