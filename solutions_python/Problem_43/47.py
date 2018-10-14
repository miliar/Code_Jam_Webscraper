

def next():
	global my_tmp
	val=my_tmp
	if my_tmp==1:
		my_tmp=0
	elif my_tmp==0:
		my_tmp=2
	else:
		my_tmp+=1
	return val

n=int(input())
out=open("out","w")

for case_n in range(n):
	st=input()
	my_tmp=1
	map={}
	for c in st:
		if c not in map:
			map[c]=next()

	
	#Find base	
	if my_tmp==0 or my_tmp==1:
		base=2
	else:
		base=my_tmp
		
	#Value
	tot=0
	for i, c in enumerate(st[::-1]):
		tot+=map[c]*(base**i)
	out.write("Case #{0}: {1}\n".format(case_n+1, tot))
		
	
		
	
	
