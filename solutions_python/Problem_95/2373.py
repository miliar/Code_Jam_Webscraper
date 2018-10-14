d=eval("{'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q', 'q':'z',' ':' '}")


T=int(raw_input())
f=open('A-small-out.txt','w')
for t in xrange(1,T+1):
	
	r=""
	s=raw_input()
	r='Case #%d: ' % (t)
	for c in s:
		r+=d[c]
	print r
	f.write(r+'\n')

