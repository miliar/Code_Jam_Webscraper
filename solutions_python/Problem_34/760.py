f = open('A-large.in',"r")
lines = f.readlines()

plines = []
for line in lines:
    plines.append( line.split('\n')[0] )

init = plines[0].split(' ')
L = int( init[0] )
D = int( init[1] )
N = int( init[2] )

words = plines[1:D+1]
cases = plines[D+1:D+N+1]

def annul(aline, possibs):
    res = []
    delete = []
    for n in xrange(len(aline)):
        rule = aline[n]
        for i in xrange(len(possibs)):
            char = words[possibs[i]][n]
            if char not in rule:
                if possibs[i] not in delete:
                    delete.append(possibs[i])
    for i in xrange(len(possibs)):
        if possibs[i] not in delete:
            res.append(possibs[i])
    return res


def annul2(aline, possibs):
    for n in xrange(len(aline)):
        rule = aline[n]
        delete = []
        for i in xrange(len(possibs)):
            char = words[possibs[i]][n]
            if char not in rule:
                delete.append(possibs[i])
        for d in delete:
            possibs.remove(d)
    return possibs                
                    

f = open('output',"w")

# parse cases
for nn,case in enumerate(cases):
    possibs = []
    for i in xrange(len(words)):
        possibs.append(i)
    # create aline
    r = False
    aline = []
    range = []
    z = 0
    for i in case:
        if i == '(':
            r = True
        elif i == ')':
            r = False
            str = ''.join(range)
            aline.append(str)
            range = []
            str = ''
            z += 1
        elif r == True:
            range.append(i)
        else:
            aline.append(i)

    possibs = annul2(aline,possibs)
    f.write("Case #%d: %d\n" % (nn+1,len(possibs)))
    print nn
    
    
