test_cases = int(raw_input(''));

for case in xrange(test_cases):
	[string, flipperSize] = raw_input('').split(' ');
	flipperSize = int(flipperSize); string = [c for c in string];
	count = 0;
	size = len(string);
	for i in xrange(size-1, flipperSize-2,-1):
		if (string[i] == '-'):
			count+=1;
			for j in xrange(i, i-flipperSize, -1):
				if (string[j] == '-'): 
					string[j] = '+'; 
				else:
					string[j] = '-';
					
	if '-' not in string[:flipperSize]:
		print 'Case #' + str(case+1) + ': ' + str(count);
	else:
		print 'Case #' + str(case+1) + ': IMPOSSIBLE';