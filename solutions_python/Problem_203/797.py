
'''
Created on Apr 12, 2013

@author: herman
'''

import copy

infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

def get_open(cake,R,C):
    for i in xrange(R):
        for j in xrange(C):
            if cake[i][j] == '?':
                return (i,j)
    return None

def attempt_move(init,spot,cake,span,R,C):
    rspan,cspan = span[init]
    nrspan = rspan[:]
    ncspan = cspan[:]
    x,y = spot

    if x < nrspan[0]:
        nrspan[0] = x
    if x >= nrspan[1]:
        nrspan[1] = x+1
    if y < ncspan[0]:
        ncspan[0] = y
    if y >= ncspan[1]:
        ncspan[1] = y+1

    ncake = copy.deepcopy(cake)
    nspan = copy.deepcopy(span)
    nspan[init] = (nrspan,ncspan)
        
    # check if clear
    for j in range(nrspan[0],nrspan[1]):
        for k in range(ncspan[0],ncspan[1]):
            if not (ncake[j][k] == init or ncake[j][k] == '?'):
                return None
            ncake[j][k] = init
    return make_move(ncake,nspan,R,C)

def make_move(cake,span,R,C):
    next_spot = get_open(cake,R,C)
    if next_spot == None:
        return cake
    else:
        for init in span.keys():
            new_cake = attempt_move(init,next_spot,cake,span,R,C)
            if not new_cake == None:
                return new_cake

def make_cake(cake,R,C):
    span = {}
    for i in xrange(R):
        for j in xrange(C):
            if not cake[i][j] == '?':
                span[cake[i][j]] = ([i,i+1],[j,j+1])
    return make_move(cake,span,R,C)

for i in xrange(trials):
    R,C = [int(x) for x in infile.readline().strip().split()]
    cake = []
    for j in xrange(R):
        cake.append(list(infile.readline().strip()))

    new_cake = make_cake(cake,R,C)
    s = "Case #%d:\n" % (i+1)
    for i in xrange(R):
        s += "".join(new_cake[i])
        s += "\n"
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
