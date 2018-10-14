#Reading Input file
f = open('A-small-attempt0.in', 'r')


#_____________________________Application Logic__________________________________
#T=int(raw_input())
T=int(f.readline())
print T
res=[]
i=0
while i<T:
	[a,shyList] = f.readline().split()
	a=int(a)
	#Current shyness position
	pos=0
	#number of people standing
	ns =0
	#Frends Required
	fr=0
	j=0
	while pos<=a:
		#print int(shyList[pos])
		if int(shyList[pos])>0:
			if ns < pos:
				#print '------'+str(ns)+'---'+str(pos)
				fr += (pos-ns)
				ns+=fr
			ns+=int(shyList[pos])
		pos+=1
	print fr
	res.append(fr)
	#parent loop
	i+=1
#________________________________________________________________________________

#Printing output in file
f1 = open('fs2.out', 'w')
i=0
while i < T :
	f1.write("Case #"+str(i+1)+": "+str(res[i]))
	
	if not i == (T-1):
		f1.write('\n')
	i=i+1
f.close()
f1.close()
