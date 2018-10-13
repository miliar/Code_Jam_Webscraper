import sys

f = open( sys.argv[1] )
f.readline()
t = 1
for l in f:
    s = [int(x) for x in l.split()[1]]
    added = 0
    standing = 0
    for i,level in zip(s,range(len(s))):
        if i:
            if standing >= level:
                standing += i
            else:
                added += (level-standing)
                standing += added + i
    print "Case #{}: {}".format(t,added)
    t += 1
f.close()
