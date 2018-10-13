
def flip(l,k,pos):
	
	for i in range(pos, pos+k):
		if l[i] == '-':
			l[i] = '+'
		elif l[i] == '+':
			l[i] = '-'
		else:
			print "Input Error"


	return l

if __name__ == "__main__":

	t = int(raw_input())
	for i in range(1, t+1):
		s,k = [s for s in raw_input().split(" ")]
		k = int(k)
		#algo: start with first minus and flip k, then look for first minus and so on
		#until reach len(s)-k+1
		l = list(s)
		try:
			pos = l.index('-')
		except ValueError:
			pos = len(l)
		nflips = 0
		while pos <= (len(l)-k):
			l = flip(l,k,pos)
			nflips += 1
			try:
				pos = l.index('-')
			except ValueError:
				pos = len(l) #implies all pancakes are now + so exit loop
		#when exit, all pancakes + iff pos == len(l)
		#so if pos is between (len(l)-k+1,len(l)) then "impossible"
		if pos == len(l):
			a = str(nflips)
		else:
			a = "IMPOSSIBLE"

			
		print "Case #" + str(i) + ": " + a





