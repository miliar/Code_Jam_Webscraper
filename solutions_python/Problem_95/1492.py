import sys

code = {};
code['a'] = 'y';
code['b'] = 'h';
code['c'] = 'e';
code['d'] = 's';
code['e'] = 'o';
code['f'] = 'c';
code['g'] = 'v';
code['h'] = 'x';
code['i'] = 'd';
code['j'] = 'u';
code['k'] = 'i';
code['l'] = 'g';
code['m'] = 'l';
code['n'] = 'b';
code['o'] = 'k';
code['p'] = 'r';
code['q'] = 'z';
code['r'] = 't';
code['s'] = 'n';
code['t'] = 'w';
code['u'] = 'j';
code['v'] = 'p';
code['w'] = 'f';
code['x'] = 'm';
code['y'] = 'a';
code['z'] = 'q';

n = int(sys.stdin.readline())
for i in range(0, n):
	ln = list(sys.stdin.readline())
	lnlen = len(ln)
	for j in range(0, lnlen-1):
		if ln[j]!=' ' and ln[j]!='\n':
			ln[j] = code[ln[j]]
		if ln[j]=='\n':
			ln[j]  = ""
	print "Case #" + str(i+1) + ": " + "".join(ln)