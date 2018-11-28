import sys

tree = {}
working = True

f = open(sys.argv[1],"r")

testcases = int(f.readline())
for i in range(1,testcases+1):
    line = f.readline().strip().split()
    givens = int(line[0])
    needed = int(line[1])
    tree = {}
    for j in range(givens):
        subdirs = f.readline().strip().split('/')
        cur = tree
        while len(subdirs) > 0:
            if cur.has_key(subdirs[0]):
                cur = cur[subdirs.pop(0)]
            else:
                cur[subdirs[0]] = {}
                cur = cur[subdirs.pop(0)]
    count = 0
    #print tree
    for k in range(needed):
        subdirs = f.readline().strip().split('/')
        cur = tree
        while len(subdirs) > 0:
            if cur.has_key(subdirs[0]):
                cur = cur[subdirs.pop(0)]
            else:
                if subdirs[0] != '':
                    count+=1
                cur[subdirs[0]] = {}
                cur = cur[subdirs.pop(0)]
        #print tree
    print "Case #%d: %d" % (i,count)
