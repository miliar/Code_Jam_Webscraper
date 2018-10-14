import sys
n=int(sys.stdin.readline())
for i in range(0,n):
	c,F,x=map(float,(sys.stdin.readline()).split())
	f=F
	count = 0 
	total = x/2      
        temp = c/2
	if (temp+(x/(2+f))) < total:
		total = c/2
		f = F + 2
		temp = temp + c/f
		count = count +1
	else:	
		print "Case #" + str(i+1) + ": " + '{0:.7f}'.format(total)
	while count>0:
		total = total + x/f
		if (temp+(x/(f+F))) < total:
                	total = temp
                	f = F + f
			temp = temp + c/f
                	count = count +1
        	else:
                	print "Case #" + str(i+1) + ": " + '{0:.7f}'.format(total)
			count = 0

