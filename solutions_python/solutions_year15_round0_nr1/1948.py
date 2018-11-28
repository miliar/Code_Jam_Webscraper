import sys

def main():
    f = open(sys.argv[1])
    fw = open(sys.argv[2], "w")
    t = int(f.readline().strip())
    for i in xrange(t):
	line = f.readline()
	sp = line.split()
	smax = int(sp[0])
	ar = [int(c) for c in sp[1]]
	p = 0
	cursum = 0
	for j in xrange(len(ar)):
	    if ar[j] > 0:
		if cursum >= j:
		    cursum += ar[j]
		else:
		    p += j-cursum
		    cursum = j
		    cursum += ar[j]
	fw.write("Case #"+str(i+1)+": "+str(p)+"\n")
    fw.close()
    f.close()

if __name__ == "__main__":
    main()
