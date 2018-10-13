import sys

sys.setrecursionlimit(200000)

def recurse(currate, price, extrarate, target):
	if (target/currate < price/currate + target/(currate+extrarate)):
		return (target/currate)
	r = (price/currate) + recurse(currate+extrarate, price, extrarate, target)
	return r
	
def mainrecurse(fname):
	f = open(fname, 'r')
	numcases = int((f.readline()))
	o = open('output.txt', 'a')
	for i in range(numcases):
		inputs = map(float, (f.readline().split()))
		result2 = recurse(2, inputs[0], inputs[1], inputs[2])
		o.write('Case #%d: %.7f\n' % (i+1, result2))
							
if __name__ == "__main__":
	mainrecurse(sys.argv[1])
	
