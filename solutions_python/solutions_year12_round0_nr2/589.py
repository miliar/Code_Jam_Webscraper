from random import shuffle,randint

def max_scores_above_p(scores, num_surprising, p):
	total = 0
	#scores = sorted(scores, reverse=True)
	for score in scores:
		small = score / 3
		med = (score - small) / 2
		big = score - med - small
		
		gtp = False
		if big >= p:
			total += 1
		elif big == small: # 000 -> -101
			if small > 0 and big < 10 and big + 1 >= p:
				gtp = True
		elif big == med: # 011 -> 002
			if big < 10 and big + 1 >= p:
				gtp = True
		if gtp:
			num_surprising -= 1
			if num_surprising >= 0:
				total += 1
	return total

def main():
	T = int(raw_input()) # num test cases
	for case in xrange(1, T + 1):
		line = [int(d) for d in raw_input().split()]
		N = line[0] # num googlers
		S = line[1] # num surprising triplets
		p = line[2] # score bound
		scores = line[3:] # score totals
		print "Case #%d: %d" % (case, max_scores_above_p(scores, S, p))

if __name__ == "__main__":
	main()

