#!/bin/python

filename = "A-large"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")

T = int(infile.readline())
for case in xrange(T):
    N, M = map(int, infile.readline().split())
    existing = [infile.readline().strip() for i in xrange(N)]
    toMake = [infile.readline().strip() for i in xrange(M)]
    
    dirs = {}
    mkdirs = 0
    for ex in existing:
        #print "Adding existing dir %s" % ex
        folders = ex.split('/')[1:]
        root = dirs
        for f in folders:
            #print "Root:"
            #print dirs
            #print "Folder: %s" % f
            if f not in root:
                root[f] = {}
                root = root[f]
            else:
                root = root[f]
                
    for ex in toMake:
        #print "Adding NEW dir %s" % ex
        folders = ex.split('/')[1:]
        root = dirs
        for f in folders:
            #print "Root:"
            #print dirs
            #print "Folder: %s" % f
            if f not in root:
                mkdirs += 1
                root[f] = {}
                root = root[f]
            else:
                root = root[f]
    
    outfile.write("Case #%d: %d\n" % (case+1, mkdirs))

infile.close()
outfile.close()