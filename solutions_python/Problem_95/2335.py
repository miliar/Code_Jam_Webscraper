a = { 'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z' }

if __name__ == "__main__":
	T = int(raw_input())
	for i in xrange(1,T+1):
		line = raw_input()
		nline = ""
		for j in xrange(0,len(line)):
			if line[j] != ' ':
				nline += a[line[j]]
			else:
				nline += ' '
		print "Case #%s: %s" % (i,nline)