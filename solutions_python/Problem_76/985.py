#candy splitting -yogesh mangaj
import sys, os

f = open('C-small-attempt2.in', 'r')
t = f.readline() #no. of test cases
i = 0
for i in range(0,int(t)):
	highest = 0
	n = f.readline() #no. of candies
	candies =  map(int,f.readline().split())
	if len(candies)<n:
		n=len(candies)
	for j in range(0,int(n)):
		for k in range(0,int(n)):
			fh,lh=0,0	#patricks sums
			for l in range(0,k):
				fh = fh^candies[l]
			for m in range(k,int(n)):
				lh = lh^candies[m]
			if fh==lh and fh==lh!=0:
				sf,sl=0,0 #seans sums
				for x in range(0,k):
					sf=sf+candies[x]
				for y in range(k,int(n)):
					sl=sl+candies[y]	

				if sf>highest:
					highest=sf
				
	

		temp = candies[0]
		candies[0:1]=[]
		candies.append(temp)
	if highest==0:
		print "Case #%d: NO" %(i+1)
	else:
		print "Case #%d: %d" %(i+1, highest) 		

	
f.close()


