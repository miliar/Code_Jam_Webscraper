#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
fname="B-large.in"
file=open(fname)


out=open("out_"+fname, "w")


from pprint import pprint


nbCases=int(file.readline())
for j in range(1,nbCases+1):
	returnFirst=0
	C, F, X=file.readline().split()
	C=float(C)
	F=float(F)
	X=float(X)
	
	
	#print C
	#print F
	#print X
	cps=2
	
	origF=2
	
	
	tab2=[]
	tab3=[]
	
	tab2.append(0.0)
	#tab3.append(X/(2.0))

	while ((len(tab3)-2)<1) or tab3[len(tab3)-1]<tab3[len(tab3)-2] :
	
		#tab.append(X/cps)
		#tab.append
	
		#tab2: temps pour construire la ferme num i
		tab2.append(C/cps+tab2[len(tab2)-1])
		
		#tab3: temps pour atteindre X avec i fermes
		tab3.append(tab2[len(tab2)-2]+X/cps) #(2.0+(len(tab2)-1)*F))
		
		
		
		#tab.append(len(tab)-1)-cps*(len(tab)-1))
		
		
		cps=cps+F
		
	# print "temps pour construire la ferme num i"
	# pprint(tab2)
	# print "temps pour atteindre X avec i fermes"
	# pprint(tab3)
	try:
		if tab3[0]<tab3[1]:
			returnFirst=1
	except:
		pass
		
	if returnFirst==1:
		
		print "res",tab3[0]
		out.write(  "Case #"+str(j)+": "+str(tab3[0]))

	else:
		print "res",tab3[len(tab3)-2]
		out.write(  "Case #"+str(j)+": "+str(tab3[len(tab3)-2]))
	out.write(  "\n")
	
	#exit()
exit()
	

#tab=[]


#tab.append   #temps si on achete x fermes






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