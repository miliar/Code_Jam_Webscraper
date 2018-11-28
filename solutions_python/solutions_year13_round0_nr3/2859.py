import math;

def is_palindrome(s):
	str(s);
	if s == '':
		result = True;
	else:
		if (ord(s[0]) - ord(s[len(s)-1])) == 0:
			return is_palindrome(s[1:len(s)-1]);
		else:
			result = False;
	return result;

def checksquare(n):
	checkd = str(n).split('.');
	if len(checkd[1]) == 1:
		return int(n)
	else:
		return False;

def check(n):
	if is_palindrome(n) == True:
		raizc = checksquare(math.sqrt(int(n)));

		if raizc != False:
			if is_palindrome(str(raizc)) == True:
				return True;
			else: 
				return False
		else:
			return False;

inputfile = open("C-small-attempt0.in", "r");
inputb = inputfile.readlines();
results = [];

for x in xrange(1, int(inputb[0]) + 1):
	
	interval = inputb[x].split();
	valid = [];

	for us in xrange(int(interval[0]), int(interval[1]) + 1):

		result = check(str(us));

		if result == True:
			valid.append(us);

	stadd = 'Case #' + str(x) + ': ' + str(len(valid));
	results.append(stadd);

resultfile = open('result.txt', "w");
resultfile.writelines(["%s\n" % item  for item in results]);
resultfile.close()