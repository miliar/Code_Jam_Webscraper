import sys

d = {'a' : 'y', 'b':'n', 'c':'f', 'd':'i', 'e':'c', 'f':'w', 'g':'l', 'h':'b', 'i':'k', 'j':'u', 'k':'o', 'l':'m', 'm':'x', 'n':'s', 'o':'e', 'p':'v', 'q':'z', 'r':'p', 's':'d', 't':'r', 'u':'j', 'v':'g', 'w':'t', 'x':'h', 'y':'a', 'z':'q' }
rev_dict = dict((v,k) for k,v in d.iteritems())

for i, line in enumerate(sys.stdin):
	if i == 0:
		continue
	print "Case #" + str(i) + ": ",
	for char in line:
		try:
			sys.stdout.write(rev_dict[char])
		except KeyError:
			sys.stdout.write(char)