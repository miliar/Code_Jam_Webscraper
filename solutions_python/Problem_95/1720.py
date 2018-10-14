import string
import sys

#Method for replacing characters
def translate(text):
	dict = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', \
			'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', \
			'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', \
			'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', \
			'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}

	newchars = []
	
	for i in xrange(len(text)):
		c = text[i]
		
		if c in dict:
			newchars.append(dict[c])
		else:
			newchars.append(c)
		
	return string.join(newchars,'')


#Standard CodeJam input munching
def codejam(fun):
	lines = sys.stdin.readlines()
	numlines = int(lines[0])

	for i in xrange(1,numlines+1):
		ans = string.join(["Case #", str(i), ": ", fun(lines[i])],'')
		sys.stdout.write(ans)

codejam(translate)
