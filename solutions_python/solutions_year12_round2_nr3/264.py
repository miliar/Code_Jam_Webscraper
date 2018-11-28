#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
fname="C-small-attempt0.in"
file=open(fname)


out=open("out_"+fname, "w")


from pprint import pprint

nbVal=20

def valeur(n, tab):
	out=0
	#print "n",n
	#print(tab)
	global nbval
	for i in range(nbVal-1,-1,-1):
		#print "currenti",i
		if n-2**i>=0:
			#print i,tab[i]
			out=out+tab[i]
			#print "+"+str(tab[i])
			n=n-2**i
		
	#print ">",out
	return out
#print valeur(3,[1,2])
#exit()
#assert(valeur(3,[1,2])==3)
	
	
def test(line,k):
	tabSols={}
	for i in range(1,2**nbVal):
		#print "i",i
		num=valeur(i, line)
		#print "num",num
		sols=tabSols.get(num,[])
		for j in sols:
			print "testing ",i,j
			if i & j == 0:
				
				out.write("Case #"+str(k)+":\n"+produceStringSolution(i,line)+"\n"+produceStringSolution(j,line)+"\n")
				print("Case #"+str(k)+":\n"+produceStringSolution(i,line)+"\n"+produceStringSolution(j,line)+"\n")

				return 
		print "rate"
		newtab=tabSols.get(num,[])
		newtab.append(i)
		tabSols[num]=newtab
		#pprint(tabSols)
	print "Case #"+str(k)+":\nImpossible\n"
	out.write("Case #"+str(k)+":\nImpossible\n")
	return 
	
	
	
	
def produceStringSolution(n,tab):
	out=""
	for i in range(nbVal,-1,-1):
		if n-2**i>=0:
			out=out+" "+str(tab[i])
			n=n-2**i
	return out
	
nbCases=int(file.readline())
for k in range(1,nbCases+1):
	line=file.readline()
	
	line=line.split()
	line=line[1:]
	line=map(int,line)
	#from pprint import pprint
	#pprint(line)
	
	
	
	test(line,k)
	
out.close()

#def m(l):
