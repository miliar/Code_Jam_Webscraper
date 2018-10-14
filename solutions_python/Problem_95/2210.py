d = {'y':'a',
	 'n':'b',
	 'f':'c',
	 'i':'d',
	 'c':'e',
	 'w':'f',
	 'l':'g',
	 'b':'h',
	 'k':'i',
	 'u':'j',
	 'o':'k',
	 'm':'l',
	 'x':'m',
	 's':'n',
	 'e':'o',
	 'v':'p',
	 'z':'q',
	 'p':'r',
	 'd':'s',
	 'r':'t',
	 'j':'u',
	 'g':'v',
	 't':'w',
	 'h':'x',
	 'a':'y',
	 'q':'z'}

T = int (input ())

for t in range (T):
	line = input ()
	s = ""
	for c in line:
		if c in d:
			s += d [c]
		else:
			s += c
	print ("Case #" + str (t + 1) + ": " + s)