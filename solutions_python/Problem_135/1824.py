import sys

tcs = int(sys.stdin.readline())

for i in range(1,tcs+1):
    prospective = set(range(1,17))
    for k in range(0,2):
        selected = int(sys.stdin.readline())    
        for j in range(1,5):
            if j==selected:
                prospective=prospective.intersection(set([int(x) for x in sys.stdin.readline().split()]))
            else:
                sys.stdin.readline()

    if len(prospective)==0:
        print "Case #" + str(i) + ": Volunteer cheated!"
    elif len(prospective) >1:
        print "Case #" + str(i) + ": Bad magician!"
    else:
        print "Case #" + str(i) + ": " + str(iter(prospective).next())

