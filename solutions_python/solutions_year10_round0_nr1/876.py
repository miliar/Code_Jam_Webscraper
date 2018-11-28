t=input();
i=1;
while(i<=t):
	s=raw_input();
	s=s.split(' ');
	n=int(s[0]);
	k=int(s[1])+1;
	if(k%(2**n)):
		print "Case #%d: OFF"%(i);
	else:
		print "Case #%d: ON"%(i);
	i+=1;
	
