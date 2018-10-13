import sys

def readlines( filename ):
	with open(filename,'r') as f:
		return [ line.rstrip('\n') for line in f.readlines() ]

def solve( infile ):
	lines = readlines( infile )
	convert = {'e':'o','j':'u','p':'r',' ':' ','m':'l','y':'a','s':'n','l':'g','c':'e','k':'i','d':'s','x':'m','v':'p','n':'b','r':'t','i':'d','b':'h','t':'w','a':'y','h':'x','w':'f','f':'c','o':'k','u':'j','g':'v','z':'q','q':'z'}
	n = int(lines[0])
	for i in range(1, n+1 ):
		plain = "".join([convert[c] for c in lines[i]])
		print "Case #{0}: {1}".format(i, plain)

if __name__ == "__main__":
	solve( sys.argv[1] )
