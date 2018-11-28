import sys

def chunkify(word):
	letters, count = [], []
	current = None
	for i, c in enumerate(word):
		if c == current:
			count[-1] += 1
		else:
			current = c
			letters.append(c)
			count.append(1)
	return ''.join(letters), count

def get_min_moves(words):
	chunks = [chunkify(w) for w in words]
	letters = [c[0] for c in chunks]
	counts = [c[1] for c in chunks]
	
	#for w in words:
	#	print w, chunkify(w)
	if len(set(letters)) != 1:
		return None
	
	total = 0
	l = len(counts[0])
	for i in range(l):
		counts_i = [x[i] for x in counts]
		#print counts_i,
		avg = 1.0*sum(counts_i)/len(counts)
		#print i, avg,
		avg = int(round(avg))
		#print avg
		diff = sum([abs(avg - x) for x in counts_i])
		total += diff
		
	
	return total

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		N = int(raw_input())
		words = [raw_input() for _ in range(N)]
		x = get_min_moves(words)
		if x == None:
			msg = 'Fegla Won'
		else:
			msg = str(x)
		print 'Case #%d: %s' % (i+1, msg)

if __name__ == '__main__':
	main()
