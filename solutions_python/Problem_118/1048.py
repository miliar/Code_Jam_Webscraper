infile = open("input.txt", "r")
outfile = open("output.txt", "w")

def isqrt(x):
	guess = x//2
	for i in xrange(0, 10000):
		if guess==0:
			return 0
		oldguess = guess
		guess = (guess+x//guess)//2
	return guess

def ispalindrome(num):
	snum = str(num)
	l = len(snum)
	for i in xrange(len(snum)//2):
		if snum[i]!=snum[l-i-1]:
			return False
	return True

ncases = int(infile.readline())
for case in xrange(ncases):
	rangestr = infile.readline().split()
	count = 0
	AA = int(rangestr[0])
	BB = int(rangestr[1])
	a = isqrt(AA)-1
	b = isqrt(BB)+1
	if a<1:
		a = 1

	for ttt in xrange(a, b+1):
		squared = ttt*ttt
		if ispalindrome(ttt) and ispalindrome(squared) and squared>=AA and squared<=BB:
			count = count + 1

	print >>outfile, "Case #%d: %s" % ((case+1), str(count),)

infile.close()
outfile.close()