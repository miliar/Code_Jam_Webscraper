prtdir = '/home/rajkumar/google-codejam/recycle/'
input = open(prtdir+ 'input.txt','r')
output = open(prtdir+'output.txt','w')

testcases = int(input.readline())

for i in range(testcases):
	pairs = 0
	limits = [int(v) for v in input.readline().rstrip().split(' ')]
	upperlimit =[int(v) for v in list(str(limits[1]))]
	lowerlimit =[int(v) for v in list(str(limits[0]))]
	
	for j in range(limits[0],limits[1]):
		strlst = list(str(j))
		#print strlst
		numlst = [int(v) for v in strlst]
		#print numlst
		a=len(numlst)
		#print a
		for k in range(1,len(numlst)):
			#print numlst[0]
			#print numlst[k]
			if numlst[0]>numlst[k]:
				continue
			if numlst[k]>upperlimit[0]:
				continue
			if numlst[k]<lowerlimit[0]:
				continue
			numdummy = numlst[k:]+numlst[:k]
			strdummy = [str(v) for v in numdummy]
			strvaluetemp = ''.join(strdummy) 	
			intdummy = int(strvaluetemp)
			if intdummy > j:
				if intdummy<=limits[1]:
				  pairs = pairs + 1
				  print str(j) +' ' +str(intdummy)+ '  pair:' + str(pairs)
				  				  				  
	print 'pairs: ',pairs
	output.write('Case #'+ str(i+1) +': '+str(pairs)+'\r\n')	