import re

sizes = raw_input().split();
l = int(sizes[0]);
d = int(sizes[1]);
n = int(sizes[2]);
words = list();
cases = list();
caseChecker = dict();

for w in range(0, d):
	words.append(raw_input());

for ca in range(0, n):
	cases.append(raw_input());

for ca in range(0, n):
	case = re.findall(r'[a-z]|\([a-z]*\)', cases[ca]);
	for ch in range(0, l):
		case[ch] = case[ch].replace('(', '', 1).replace(')', '', 1);
	wordsCount = 0;
	caseChecker = list();
	
	for ch in range(0, l):
		caseChecker.append(dict());
		for chaz in range(0, 26):
			caseChecker[ch][chr(97 + chaz)] = False;
	for ch in range(0, l):
		for chaz in range(0, len(case[ch])):
			caseChecker[ch][case[ch][chaz]] = True;
			
	for w in range(0, d):
		word = words[w];
		result = True;
		for ch in range(0, l):
			if caseChecker[ch][word[ch]] == False:
				result = False;
				break;
		if result == True:
			wordsCount += 1;
	print 'Case #' + str(ca + 1) + ': ' + str(wordsCount);
