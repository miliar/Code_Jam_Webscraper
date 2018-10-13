import sys

infile = open('input-small-CA2.in', 'r');
outfile = open('QuestionCA2large.out', 'w');
cases = int(infile.readline());

for case in range(1,cases+1):
	ans = 0;
	line = infile.readline().rstrip("\n\r").split();
	N = int(line[0]);
	
	
	a = [];
	b = [];
	for i in range(0,N):
		line = infile.readline().rstrip("\n\r").split();
		a.append(int(line[0]));
		b.append(int(line[1]));
	
	ans = 0;
	for i in range(0,len(a)):
		for u in range(0,len(b)):
			if i != u:
				if (a[i] < a[u]):
					if (b[i] > b[u]):
						ans+=1;

	ans = str(ans);

	print "Case #" + str(case) + ": " + str(ans)
	outfile.write("Case #" + str(case) + ": " + str(ans) + "\n");
outfile.close();