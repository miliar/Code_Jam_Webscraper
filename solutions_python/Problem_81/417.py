import sys
test = sys.stdin.readlines()

def find_max_combi(t):

    return 

ncases = int(test[0].rstrip('\n'))
for i in range(1, 2*ncases,2):
    vals_s = test[i+1].rstrip('\n').split(' ')
    vals = [int(v) for v in vals_s]
    r = 0
    for v in vals:
        r = r^v
    if r:
        print "Case #" + str(i/2+1) + ": NO"
    else:
        print "Case #" + str(i/2+1) + ": " + str(find_max_combi(vals))

