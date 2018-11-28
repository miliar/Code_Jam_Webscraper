import re

if __name__ == "__main__":
	fin = open("A-large.in", "r")
	fout = open("A-large.out", "w")
	
	L, D, N = map(int, fin.readline().split())
	#print L, D, N
	
	words = []
	for d in xrange(0, D):
		words.append(fin.readline().replace('\n', ''))
	#print words
	
	for req in xrange(0, N):
		pat = "^" + fin.readline().replace('\n', '').replace('(', '[').replace(')', ']') + "$"
		pat = re.compile(pat);
		
		ans = 0
		for text in words:
			if pat.match(text):
				ans = ans+1
				
		fout.write("Case #%d: %d\n" % (req+1, ans))
