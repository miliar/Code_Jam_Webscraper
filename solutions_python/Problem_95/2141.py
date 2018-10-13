from string import maketrans
import sys

def trans(input):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	trans = "yhesocvxduiglbkrztnwjpfmaq"
	transtab = maketrans(alpha,trans)
	return input.translate(transtab)

if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for s in xrange(t):
		inp = f.readline()
		print "Case #%d: %s" %(s+1,trans(inp).strip())