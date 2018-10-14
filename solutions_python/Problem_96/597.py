def compute():
	f=open("B-large.in");
	lines = f.readlines()
	i = 1;
	
	for line in lines[1:]:
		line = line.replace('\n','');
		contents = line.split(' ');
		numMen = int(contents[0]);
		numSurp = int(contents[1]);
		bestScore = int(contents[2]);
		numValues = [int(x) for x in contents[3:]]
		numValues.sort();
		currCount = 0;
		for value in numValues:
			canCreate, numSurp = cangenerate(value, bestScore, numSurp)
			if canCreate == 1:
				currCount = currCount + 1;
		print "Case #"+str(i)+":",currCount;
		i = i +1;


def cangenerate(total, minValue, remaininSurp):
	v1 = total/3;
	v2 = total%3;
	
	if(minValue<=v1):
		return 1, remaininSurp;

	if v2 == 0:
		if(remaininSurp == 0):
			if(minValue <= v1):
				return 1, remaininSurp;
			else:
				return 0, remaininSurp;
		else:
			if(minValue <= v1+1) and v1 != 0:
				return 1, remaininSurp - 1;
			else:
				return 0, remaininSurp;
	else:
		if v2 == 1:
			if(minValue <= v1 + 1):
				return 1, remaininSurp;
			else:
				return 0, remaininSurp;
		else:
			if(remaininSurp == 0):
				if(minValue <= v1+1):
					return 1, remaininSurp;
				else:
					return 0, remaininSurp;
			else:
				if(minValue <= v1+2):
					return 1, remaininSurp - 1;
				else:
					return 0, remaininSurp;
			
	
compute();
