
t=int(raw_input())
f=open('output.txt','w')
for i in xrange(0,t):
	n,s=raw_input().split(' ')
	noofpeostand=int(s[0])
	noofpeoneed=0
	for j in xrange(1,len(s)):
		
		if(s[j]!='0'):
			if(j>noofpeostand):
			
				temp=-noofpeostand+j
				noofpeostand=noofpeostand+temp+int(s[j])
				noofpeoneed=noofpeoneed+temp
			else:
			
				noofpeostand=noofpeostand+int(s[j])
		
	
	f.write("Case #%d: %d\n"%(i+1,noofpeoneed))
	print "Case #%d: %d"%(i+1,noofpeoneed)
	