import sys

tmap = { 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 
	'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 
	'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 
	'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 
	't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm',
	'q':'z' , 'z': 'q', ' ': ' ' }

N = int(raw_input().strip())

for i in range(1,N+1):
	line = raw_input().strip()
	sys.stdout.write("Case #"+str(i)+": ")
	for c in line:
		sys.stdout.write(tmap[c])
	print ""