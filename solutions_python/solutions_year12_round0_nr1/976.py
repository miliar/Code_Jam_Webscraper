#!python
import sys
import string

def main(*args):
	if len(args) < 2:
		print "Usage:\n", args[0], " <file>\n"
		return
	file = open(args[1])
	text = file.read().split('\n')
	arr = list(text)
	#print arr
	#googlerese = {a:y, b:h, c:e, d:s, e:o, f:c, g:, h:x, i:d, j:u, k:i, l:g, m:l, n:b, o:k, p:r, q:z, r:t, s:n, t:w, u:j, v:p, w:f, x:m, y:a, z:}	
	table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq') #left - gz -> vq
	#table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocqxduiglbkrztnwjpfmav') #left - gz -> qv
	cases = int(arr[0])
	#if cases != len(arr) - 1:
	#	print "Error"
	i = 1
	while i <= cases:
		print "Case #%s: %s" % (i,string.translate(arr[i], table))
		i += 1

if __name__ == '__main__':
    sys.exit(main(*sys.argv))