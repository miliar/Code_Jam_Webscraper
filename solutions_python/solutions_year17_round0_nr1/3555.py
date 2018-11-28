cases=int(raw_input())
j=1

def flip(list,i,j):
	#print f
	#print len(list[i:j])
	global flag
	flag=0
	global count
	if f<=len(list[i:j]):
		for k in range(i,j):
			if(list[k]=='-'):
				list1[k]='+'
			else:
				list1[k]='-'
		count=count+1
	    

	
while j<=cases:
	pancakes=raw_input()
	list2=pancakes.split(" ")
	f=int(list2[1])
	count=0
	list1=list(list2[0]);	
	for i in range(len(list1)):
		if list1[i]=='+':
			list1[i]='+'
		else:
			flip(list1,i,i+f)
	
	if '-' in list1:
		print "Case #%d: IMPOSSIBLE" %(j)
	else:
		print "Case #%d: %d" %(j,count)
	j=j+1