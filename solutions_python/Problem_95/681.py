


def translate(line):
	translator = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
	rets = ""
	for i in xrange(len(line)):		
		try:
			rets += translator[line[i]]
		except:
			rets += line[i]
	return rets

def translate_back(line):
	translator = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
	revtrans = dict(zip(translator.values(),translator.keys()))		
	rets = ""
	for i in xrange(len(line)):		
		try:
			rets += revtrans[line[i]]
		except:
			rets += line[i]
	return rets



def get_problems():
	f = file("A-small-attempt0.in")
	numCases = f.readline()
	for i in xrange(1, int(numCases)+1):
		line = f.readline()
		output = translate(line)
		print "Case #%d:" % i, output

get_problems()



