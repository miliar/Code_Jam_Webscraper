


def checkScore(g, s, p):
    if g == 0 and p > 0:
        return (0, 0)
    x = [g / 3]
    x = [g / 3, (g - (g / 3)) / 2, g - (((g - (g / 3)) / 2) + (g / 3))]
    x.sort()
    if x[2] >= p:
        return (1, 0)
    if s:
        if (g % 3 == 2) or (g % 3 == 0): #we can subtract one from x[1]
            if (x[2] + 1) >= p:
                return (1, 1)
        #if g % 3 == 1 can't do anything
    return (0, 0) #couldn't match that shite


if __name__=='__main__':
    f = open("P-Binput.txt", "r")
    outsies = open("P-Boutput.txt", "w")
    lines = f.readlines()
    t = int(lines[0].rstrip())
    for i in xrange(t):
        line = [int(a) for a in lines[i+1].rstrip().split()]
        n, s, p = line[0], line[1], line[2]
        v = 0
        for g in xrange(n):
            test = checkScore(line[g+3], s, p)
            if(test[1]):
                s -= 1
            if(test[0]):
                v += 1
        outsies.write("Case #{0}: {1}\n".format(i+1, v))

