#! /usr/bin/python

def min_secs(i):
	tempList = input().split();
	
	C = float (tempList[0]);
	F = float (tempList[1]);
	X = float (tempList[2]);

	#intially at the increase rate to 2.
	r = 2.0 ;
	#time takes for producing X cookies at the rate of r.
	T1    = X/r;
	total = 0.0;             # intialize total to zero.
	
	while True:  # Loop forever
		Tcr  = C/r;          # Time taken for producing C cookies at rate of r. 
		Txrf = X/(r+F);      # Time taken for producing X cookies at the rate of r+F.
		T2   = Tcr + Txrf;
		if T2 < T1:
			total += Tcr;
			r      = r + F;  
		else:
			total += X/r;
			break;
		T1 = Txrf;
	
	print ("Case #%d: %.7f" %(i, total));    	
	return

totalTestCases = int (input());
for i in range(0, totalTestCases):
	min_secs(i+1);