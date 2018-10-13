"""C
   Google CodeJam 2009
"""

from datetime import datetime

FIND = "welcome to code jam"
        
count = 0
        
def countall(cplaces, zi, prev):
    global count
    #print "countall", zi, prev
    #print prev,
    if zi >= len(cplaces):       
        #print "Found"
        count += 1
        return True #made it
    for place in cplaces[zi]:
        if place < prev:
            #"Not found"
            continue #failed
        if not countall(cplaces, zi+1, place):
            print "prune"
            break  #prune
    return True
        
def routine(text):
    found = 0
    
    #find individial characters
    
    cplaces = []
    for ci, c in enumerate(FIND):
        places = []
        
        i = 0
        if ci > 0:
            if cplaces[ci - 1]:
                i = cplaces[ci-1][0]  #start after 1st of previous char
        p = text.find(c, i)
        while p > -1:
            places.append(p)
            i = p+1
            p = text.find(c, i)
        
        if ci > 0:
            if places:
                for p in cplaces[ci - 1]:
                    if p > places[-1]:
                        cplaces[ci - 1].remove(p)
        
        if not places:
            print "short-circuit: no appropriate '%s'" % c
            return 0    #short-circuit: we have a missing char
                        
        cplaces.append(places)
        
    for x in cplaces:
        print x
    
    #count all sequential matches
    global count
    count = 0
    found = countall(cplaces, 0, None)
    
    print count
    
    return count

if __name__ == '__main__':
    filename = "C-small-attempt2" #C-small
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline())
    print c, "cases"
    for case in xrange(c):
        text = f.readline()

        print text

        print
        print >>fo, "Case #%d: %s" % (case+1, ("%04d" % routine(text))[-4:])

    fo.close()
    f.close()
    print datetime.now()
