inputFile = "B-large.in";
outputFile = "B-large.out";

def main():	
	fdin = open(inputFile);
	fdout = open(outputFile, 'wb');
	
	casecountString = fdin.readline();
	caseCount = int(casecountString);
	
	for k in range(caseCount):
		number = int(fdin.readline());
		result = getNext(number);
		resultLine = "Case #" + str(k+1) +": " +result + "\n";
		fdout.write(resultLine);
		
def getNext(n):
	m1=n%10;
	n=n/10;
	list = {};
	list[m1]=1;
	while True:
		m=n%10;
		n=n/10;
		if list.has_key(m):
			list[m]=list[m]+1;
		else:
			list[m]=1;
		IsMax = True;
		for i in range(m+1, 10):
			if list.has_key(i) and list[i] > 0:
				IsMax = False;
				larger = i;
				break;
		if not IsMax:
			r = larger;
			for j in range(10):
				c=0;
				if list.has_key(j) and list[j]>0:
					if j == larger:
						c = list[j] -1;
					else:
						c = list[j];
				for k in range(c):
					r=r*10 + j;
			if n ==0:
				base="";
			else:
				base=str(n);
			return  base + str(r);
		
			
		
		
if __name__ == "__main__":
    main()