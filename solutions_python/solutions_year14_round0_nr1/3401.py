import sys

def check(pos0,pos1,l0,l1):
	a = list(set(pos0[l0-1]).intersection(pos1[l1-1]))
	if len(a) == 1:
		return a[0]
	if len(a)== 0:
		return "Volunteer cheated!"
	if len(a)>1 :
		return "Bad magician!"

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        l0=map(int,f.readline().split())
        l0 = l0[0]
        pos0 = []
        for _s in range(4):
            pos0.append(map(int,f.readline().split()))
        l1=map(int,f.readline().split())
        l1 = l1[0]
        pos1 = []
        for _s in range(4):
            pos1.append(map(int,f.readline().split()))
        print "Case #" + str(_t+1) + ": " + str(check(pos0,pos1,l0,l1))
