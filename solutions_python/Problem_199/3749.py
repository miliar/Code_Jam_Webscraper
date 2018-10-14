flip = {'-': '+', '+': '-'};

f = open('test.txt','r');
out = open('testOut.txt', 'w');
cases = int(f.readline().strip());
for i in range(1, cases+1):
	case = f.readline().strip();
	flipperLength = int(case[case.index(' '): len(case)]);
	case = list(case[0:case.index(' ')]);
	flips = 0;
	for x in range(0, len(case)-(flipperLength-1)):
		if(case[x] == '-'):
			for n in range(0, flipperLength):
				case[n+x] = flip[case[n+x]];
			flips += 1;
	if('-' in case):
		out.write('Case #' + str(i) + ': IMPOSSIBLE\n');
	else:
		out.write('Case #' + str(i) + ': ' + str(flips) + '\n');
out.close();