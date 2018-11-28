import sys, math

def main():
    f = open(sys.argv[1])

    t = int(f.readline().strip())
    for i in xrange(t):
	line = f.readline()
	sp = line.strip().split()
	n = int(sp[0])
	k = int(sp[1])

	lv = int(math.log(k, 2))

	ar = [n]	
	for j in xrange(lv):
	    nar = []
	    for elem in ar:
		if elem % 2 == 1:
		    nar.append(elem/2)
		    nar.append(elem/2)
		else:
		    nar.append(elem/2)
		    nar.append(elem/2-1)
	    ar = nar
	
	rem = k - int(math.pow(2,lv))+1
	fullflag = False	
	m1 = 0
	m2 = 0

	for j in xrange(rem):
	    ar = sorted(ar, reverse=True)
	    if ar[0] == 0:
		fullflag = True
		break
	
	    if ar[0] % 2 == 1:
		ar.append(ar[0]/2)
		ar.append(ar[0]/2)
	    else:
		ar.append(ar[0]/2)
		ar.append(ar[0]/2-1)

	    if j < rem-1:
	        ar = ar[1:]

	m1 = max(ar[-1], ar[-2])
	m2 = min(ar[-1], ar[-2])

	if fullflag:
	    print "Case #"+str(i+1)+": 0 0"
	else:
	    print "Case #"+str(i+1)+": "+str(m1)+" "+str(m2)

    f.close()

if __name__ == "__main__":
    main()
