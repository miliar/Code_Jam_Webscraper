import sys

if(len(sys.argv) > 1):

	f = open(sys.argv[1])
	cases = f.readline().strip()

	for i in range((int)(cases)):
		line = f.readline().strip().split()
		#print line

		googlers = (int)(line[0])
		surprises = (int)(line[1])
		p = (int)(line[2])
		successes = 0

		#print p
		for j in range(googlers):
			score = (int)(line[3+j])

			if(p>=1):
				res = p+(p-1)+(p-1) #non-surpise
			else:
				res = 0
			if(res<=score):				
				#print (str)(score)+" res <= score"
				successes += 1
			else:
				#try surprise
				if(p>=2):
					s_res = p+(p-2)+(p-2)
				elif(p==1):
					s_res = 1
				else:
					s_res = 0
				if(s_res<=score):				
					if(surprises > 0):
						surprises -= 1 
						successes += 1
						#print (str)(score)+" res < score (surpise absorbed)"
					#else:
						#print (str)(score)+" res < score (surprise empty)"
				#else:
					#print (str)(score)+"cant work"

		print "Case #"+((str)(i+1))+": "+(str)(successes)
	
	#outfile = open('out.txt','w')
	#outfile.write(output)
	#outfile.close()




		
		

