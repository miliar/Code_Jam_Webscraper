import sys

infile = sys.argv[1]

def test(i,inf):
    s = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
    for i in range(2):
        row = int(inf.readline().strip())
        for r in range(row):
            tmp = inf.readline()
            s1 = tmp.split()
            
        for r in range(4 - row):
            inf.readline()
            
        s1 = set(s1)
        # print "s1 :",s1
        s = s & s1
        # print "s: ", s
    return s

def function(infile):
    with open(infile) as inf:
        tests = int(inf.readline())
        for i in range(tests):
            s = test(i,inf)
            if len(s) == 1:
                print "Case #%s: %s" % ((i+1),s.pop())
                continue
            if len(s) > 1:
                print "Case #%s: Bad magician!" %(i+1)
                continue
            if len(s) < 1:
                print "Case #%s: Volunteer cheated!" %(i+1)
                continue
    inf.close()

function(infile)
