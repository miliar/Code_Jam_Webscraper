
def doProb(fname, ofname):#do problem A given a file name
	f = open(fname, 'r');
	T = int(f.readline());
	output = [];
	for xx in xrange(T):        
		[X, S, R, t, N] = map(int, f.readline().split());
		Ivals = []
		total = 0;
		for i in xrange(N):
			[Bi, Ei, Wi] = map(int, f.readline().split());
			Ivals.append((Wi, Ei-Bi));
			total += Ei-Bi;
		
		Ivals.append((0, X-total));
		
		Ivals.sort()
		output.append('Case #' + str(xx+1) + ': ' + doStuff(X, S, R, t, Ivals)+'\n');
		
	f.close();  
	of = open(ofname, 'w');   
	of.writelines(output);
	of.close();   

def doStuff(X, S, R, t, Ivals):
	#step through in order, adding the neccessary things
	L = 0;
	ttot = 0;
	sr = True; #still running
	if(t==0):
		sr = False;
		
	for iv in Ivals:
		L += iv[1]
		
		if(sr):
			dLeft = (R+iv[0])*t
			if(dLeft>=iv[1]):
				val = iv[1]/(R+iv[0]);
				t -= val;
				ttot += val;
				
				if(t<1e-8):
					sr = False
			else:
				#mid-way through the interval
				sr = False
				ttot += t;
				t = 0;
				ttot += (iv[1]-dLeft)/(S+iv[0]);
								
		else: 
			ttot += iv[1]/(S+iv[0]);
			
	#if(sr):
#		dLeft = R*t;
#		if(dLeft>X-L):
#			ttot += (X-L)/R;
#		else:
#			ttot += t;
#			ttot += (X-L-dLeft)/S;			
#	else:
#		ttot += (X-L)/S;	
#				
	return str(ttot)
		
	
#doProb('a.in', 'a.out')
doProb('A-large.in', 'A-large.out')
#doProb('A-small.in', 'A-small.out')
