def inversion(n,index):
	for i in range(index,-1,-1):
		if n[i] > n[i+1]:
			n[i]-=1
			n[i+1] = 9
	return n[:index+2]




for l in range(input()):
	print "Case #"+str(l+1)+":",
	n = map(int,list(str(input())))

	
	for i in range(len(n)-1):
		if n[i] > n[i+1]:
			temp = inversion(n,i)
			for j in range(i+2,len(n)):
				temp.append(9)
			n = temp
			break
# 45553 53    
# 45550
# 44999
	if n[0]==0:
		n = n[1:]
	n = map(str,n)
	print ''.join(n)

