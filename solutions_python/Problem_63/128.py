import sys
import math

infile = open('input-small-CB.in', 'r');
outfile = open('QuestionCBlarge.out', 'w');
cases = int(infile.readline());

L,P =0,0;

def getMax (m, num):
	global L, P;
	sm = m;
	snum = num;
	ans = 0;
	#print m, num
	if (m >= num):
		return 0;
	while True:
		num = math.ceil(num / C);
		m = m * C;
		if m >= num:
			return 1 + min(getMax(m,snum), getMax(sm,num));
	return 0 ;		

for case in range(1,cases+1):
	ans = 0;
	line = infile.readline().rstrip("\n\r").split();
	L = int(line[0]);
	P = int(line[1]);
	C = int(line[2]);
	
	if P > C * L:
		#ans = int(math.floor(math.log(math.floor((P - L) / C))) / math.log(2) / 2);
		num = P * 1.0;
		m = L * 1.0;
		ans = getMax(m, num/C);
			
				

	ans = str(ans);

	print "Case #" + str(case) + ": " + str(ans)
	outfile.write("Case #" + str(case) + ": " + str(ans) + "\n");
outfile.close();