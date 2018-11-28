#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
fname="dlarge.in"
file=open(fname)


out=open("out_"+fname, "w")


from pprint import pprint
nbCases=int(file.readline())
for j in range(1,nbCases+1):
	line=file.readline()
	line=line.split()
	if debug:
		pprint(line)
	allowedAsto=int(line[1])
	compte=0
	
	if debug:
		pprint(line)
	p=int(line[2])
	for i in range(3,3+int(line[0])):
		#print i
		tot=int(line[i])
		if debug:
			print "tot: "+str(tot)
		#if tot >= p+max((p-1),0)+max((p-1),0):
		#	if debug:
		#		print str(tot)+"->OK"
		#	compte=compte+1
		#	continue
		if tot >= p+max((p-1),0)+max((p-1),0):
			if debug:
				print str(tot)+"->OK"
			compte=compte+1
			continue
		
        
			
		if tot >= p+max((p-2),0)+max((p-2),0):
			if allowedAsto==0:
				if debug:
					print str(tot)+"->KO Plus de asto"
					print "rate"+str(tot)
				continue
			else:
				if debug:
					print str(tot)+"->OK coute 1 asto"
				compte=compte+1
				allowedAsto=allowedAsto-1
				continue
		
		
		#compte=compte+1
		if debug:
			print "KO trop petit "+str(tot)
	out.write("Case #"+str(j)+": "+str(compte))
	print "Case #"+str(j)+": "+str(compte)
	out.write("\n")
out.close()