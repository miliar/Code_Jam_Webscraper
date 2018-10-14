#print string[-1:]+string[:-1]
#print string[-2:]+string[:-2]
#print string[-3:]+string[:-3]

f=file('ginp','r')
l=f.readline()
#print l 
testcases=int(l.split()[0])

for case in range(1,testcases+1):
	
	inputbuffer=f.readline()
	a,b=int(inputbuffer.split()[0]),int(inputbuffer.split()[1])
	
	count=0

	for j in range(a,b+1):
		num=j
		#print num
		string=str(num)
		strlen=len(string)
		#print string,strlen,"\t",
		for i in range(1,strlen):
			buff=string[-i:]+string[:-i]
			if buff[0]!=0:
				intbuff=int(buff)
				#print len(buff)
				if intbuff>num and intbuff<b+1 and intbuff>a+1:
					#print intbuff,i,
					count+=1
		#print
	print "Case #%d:" %case,count
