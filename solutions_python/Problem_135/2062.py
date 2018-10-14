#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
fname="A-small-attempt0.in"
file=open(fname)


out=open("out_"+fname, "w")


from pprint import pprint

b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
print set(b1).intersection( set(b2) )

nbCases=int(file.readline())
for j in range(1,nbCases+1):
	ans1=file.readline()

	tab=[]
	#pprint(tab)



	tab.append(map(int, file.readline().split()))
	tab.append(map(int, file.readline().split()))
	tab.append(map(int, file.readline().split()))
	tab.append(map(int, file.readline().split()))
	#pprint(tab)

	first = tab[int(ans1)-1]

	print first
	ans2=file.readline()
	tab2=[]
	tab2.append(map(int, file.readline().split()))
	tab2.append(map(int, file.readline().split()))
	tab2.append(map(int, file.readline().split()))
	tab2.append(map(int, file.readline().split()))
	second = tab2[int(ans2)-1]
	print second
	
	pprint(set(first))
	pprint(set(second))
	#second=tab2[int(ans2)]

	res=set(first).intersection( set(second) )
	out.write(  "Case #"+str(j)+": ")
	#out.write(res)
	
	if len(res)>1:
		out.write(  "Bad magician!")
	if len(res)==0:
		out.write( "Volunteer cheated!")
	if len(res)==1:
		out.write(str(res.pop()))
	#print union 
	out.write( "\n")

exit()
line=line.split()


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