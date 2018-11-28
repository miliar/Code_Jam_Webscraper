t = int(raw_input())  
for i in xrange(1, t + 1):
	strng,num  = [str(s) for s in raw_input().split(" ")]
	#strng=strng.replace('-','0')
	#strng=strng.replace('+','1')
	n=list(strng)
	num=int(num)
	loop=-1
	count=0
	for j in range(0,len(strng)):
		if(n[j]=='-' and len(strng)-j>num-1):
			count+=1
			for k in range(0,num):
				if(n[j+k] =='-'):
					n[j+k]='+'
					
				else:
					n[j+k]='-'
		if(len(strng)-j<=num-1):
			if(n[j]=='-'):
				count='IMPOSSIBLE'
	#print (n)
	print "Case #{}: {}".format(i,count)
	

