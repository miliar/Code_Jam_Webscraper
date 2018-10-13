import sys
Googlerese = 'ynficwlbkuomxsevzpdrjgthaq'
English =    'abcdefghijklmnopqrstuvwxyz'
f = open(sys.argv[1], 'r')
input = f.readlines()
T = int(input[0])
for i in xrange(len(input)-1):
 s = list(input[i+1])
 for x in xrange(len(s)):
  for y in xrange(26):
	 if Googlerese[y]==s[x]:
		 s[x]=English[y]
		 break
 sys.stdout.write('Case #'+str(i+1)+': '+''.join(s))
