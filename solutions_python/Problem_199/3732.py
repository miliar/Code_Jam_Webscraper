ins = open("in.list", "r")
array = []
testcases = ins.readline()
for line in ins:
    array.append(line.rstrip('\n'))

#print "Testcases:", testcases

#i = 0
#while i < len(array):
#    print(array[i])
#    i += 1
for lline in range(len(array)):

	case = list(array[lline].split()[0])#.replace("+", "1").replace("-", "0")
	k = int(array[lline].split()[1])
	n = len(case)	

	#print "n=", n
	#print "k=", k
	#print "Pancakes:", "".join(case)
	#print ""	

	i = 0
	count = 0
	while i < len(case)-k+1:
	    if case[i] == "-":
	    	for kk in range(k):
	    		#print i, kk, case[i+kk]
	    		if case[i+kk] == "-":
	    			case[i+kk] = "+"	

	    		else:
	    			case[i+kk] = "-"
	    	#print i, "".join(case)
	    	count += 1
	    i += 1	

	for i in range(len(case)):
		if case[i] == "-":
			count = "IMPOSSIBLE"	

	#print array[lline]
	print "Case #%d: %s" % (lline+1, count)





