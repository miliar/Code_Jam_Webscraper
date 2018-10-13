import sys

def main():
    f = open(sys.argv[1])
    t = int(f.readline().strip())

    for i in xrange(t):
	line = f.readline().strip()
	r,c = [int(elem) for elem in line.split()]
	
	mm = []
	inds = []
	for j in xrange(r):
	    ll = [cc for cc in f.readline().strip()]
	    mm.append(ll)

	    ncol = 0
	    for cc in ll:
		if cc != "?":	
		    inds.append([cc, j, ncol])
		ncol += 1

	inds = sorted(inds, key=lambda x:(c*x[1]+x[2]), reverse=True)
	for ind in inds:
	    rpl = ind[2]-1
	    rpr = ind[2]+1
	    cpu = ind[1]-1
	    cpd = ind[1]+1

	    while rpr < c and mm[ind[1]][rpr] == "?":
		mm[ind[1]][rpr] = ind[0]
		rpr += 1

	    rpr -= 1

	    while rpl >= 0 and mm[ind[1]][rpl] == "?":
                mm[ind[1]][rpl] = ind[0]
                rpl -= 1

            rpl += 1

	    while cpd < r:
		flag = True
		for subind in xrange(rpl, rpr+1):
		    if mm[cpd][subind] != "?":
			flag = False
			break

		if flag:
		    for subind in xrange(rpl, rpr+1):
			mm[cpd][subind] = ind[0]
		    cpd += 1
		else:
		    break

	    cpd -= 1

	    while cpu >= 0:
                flag = True
                for subind in xrange(rpl, rpr+1):
                    if mm[cpu][subind] != "?":
                        flag = False
                        break

                if flag:
                    for subind in xrange(rpl, rpr+1):
                        mm[cpu][subind] = ind[0]
                    cpu -= 1
                else:
                    break

            cpu += 1


	print "Case #"+str(i+1)+":"
	for rr in mm:
	    linestr = ""
	    for cc in rr:
		linestr += cc
	    print linestr

    f.close()

        

if __name__ == "__main__":
    main()
