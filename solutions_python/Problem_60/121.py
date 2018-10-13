import sys

infile = open('B-large.in', 'r');
outfile = open('Question' + 'Bout-large' + ".out", 'w');
cases = int(infile.readline());

for case in range(1,cases+1):
	ans = 0;
	line = infile.readline().rstrip("\n\r").split();
	N = int(line[0]);
	K = int(line[1]);
	B = int(line[2]);
	T = int(line[3]);
	
	line = infile.readline().rstrip("\n\r").split();
	Xi = [];
	for i in range(0,len(line)):
		Xi.append(int(line[i]));
		
	line = infile.readline().rstrip("\n\r").split();
	Vi = [];
	for i in range(0,len(line)):
		Vi.append(int(line[i]));

	count = 0;
	time = 0;
	tydinhaal = [];
	posEnd = [];
	#print N
	for i in range(N-1, -1, -1):
		if Xi[i] + Vi[i] * (T-time) >= B and i == N-1:
			N -= 1;
			Vi = Vi[:i];
			Xi = Xi[:i];
			K -= 1;
			continue;
		posEnd.append(Xi[i] + Vi[i] * (T-time));
		if Vi[i] < Vi[i-1]:
			tydinhaal.append(-(Xi[i] - Xi[i-1])* 1.0 / (Vi[i]-Vi[i-1]));
		elif Vi[i] == Vi[i-1]:
			tydinhaal.append(0);
		else:
			tydinhaal.append(-1);
	#print N
	#if K == 0:
		#print "None!";
	posEnd.reverse();
	tydinhaal.reverse();
	#print posEnd
	allowedPass = 0;
	if K > 0:
		for i in range(N-1, -1, -1):
			#print i
			if posEnd[i] >= B:
				#print "YES", N, i, N-1-i
				ans += (N-1 - i) - allowedPass;
				allowedPass+=1;
				K -= 1;
				#if K < 0:
				#	ans += K;
				if K <= 0:
					break;
	if K > 0:
		ans = "IMPOSSIBLE";
	#print posEnd;
	#print tydinhaal
	ans = str(ans);

	print "Case #" + str(case) + ": " + str(ans)
	outfile.write("Case #" + str(case) + ": " + str(ans) + "\n");
outfile.close();