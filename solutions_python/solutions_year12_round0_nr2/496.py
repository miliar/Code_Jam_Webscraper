def score_diff (score):
	return max(score) - min(score)

def get_best (score, surprises, thresh):
	solns_reg = []
	solns_surp = []
	middle = (score / 3)

	# suck it, itertools - i'm a lazy man
	for i in xrange (middle - 2, middle + 3):
		for j in xrange (middle - 2, middle + 2):
			for k in xrange (middle - 2, middle + 2):
				soln = (i, j, k)

				if sum(soln) == score and min(soln) >= 0:
					diff = score_diff (soln)
					if diff <= 1:
						solns_reg.append (soln)
					elif diff == 2:
						solns_surp.append (soln)

	# good enough for 2am...
	if solns_reg:
		best = max(solns_reg)
		if max(best) >= thresh:
			return best

	if solns_surp and surprises > 0:
		best = max (solns_surp)
		if max(best) >= thresh:
			return best

	return None


if __name__ == "__main__":
	with open('B-large.in') as f:
		f.next() 	# skip first line
		case = 1
		for line in f:
			Ns, Ss, ps, scores = line.strip().split(' ', 3)
			scores = scores.split()
			numGooglers = int(Ns)
			surprises = int(Ss)
			p = int(ps)

			total_best = 0

			for score in scores:
				score = int(score)
				best_solution = get_best (score, surprises, p)
				if best_solution and max(best_solution) >= p:
					# ration off the number of surprising triplets
					# if we were forced to use up one
					if score_diff (best_solution) == 2:
						surprises -= 1

					total_best += 1

			print 'Case #%d: %d' % (case, total_best)
			case += 1