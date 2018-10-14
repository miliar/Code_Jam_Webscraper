'''Google CodeJam 2012 Qualification Round Part B

You're watching a show where Googlers (employees of Google) dance, and then
each dancer is given a triplet of scores by three judges. Each triplet of
scores consists of three integer scores from 0 to 10 inclusive. The judges have
very similar standards, so it's surprising if a triplet of scores contains two
scores that are 2 apart. No triplet of scores contains scores that are more
than 2 apart.

For example: (8, 8, 8) and (7, 8, 7) are not surprising.
(6, 7, 8) and (6, 8, 8) are surprising. (7, 6, 9) will never happen.

The total points for a Googler is the sum of the three scores in that
Googler's triplet of scores. The best result for a Googler is the maximum
of the three scores in that Googler's triplet of scores. Given the total
points for each Googler, as well as the number of surprising triplets of
scores, what is the maximum number of Googlers that could have had a best
result of at least p?'''

import sys

# Skip useless first line
sys.stdin.next()

def parse_input(line):
	'''Each test case consists of a single line containing integers separated by
	single spaces. The first integer will be N, the number of Googlers, and the
	second integer will be S, the number of surprising triplets of scores.
	The third integer will be p, as described above.
	Next will be N integers ti: the total points of the Googlers.'''
	data = map(int, line.split())
	S = data[1]
	p = data[2]
	t = data[3:]
	return p, t, S

def max_googlerific_googlers(threshold, totals, num_surprising):
	'''Find the maximum number of googlers who could have a best result greater
	than or equal to the threshold, given their total score and the number of
	surprising scores.
	
	The minimum non surprising score is
	p-1 + p-1 + p = 3p-2 (assuming p >= 1)

	And the minimum surprising score is
	p-2 + p-2 + p = 3p-4 (assuming p >= 2)

	where p is the threshold
	'''
	max_non_surprising = 0
	max_surprising = 0
	for total in totals:
		if threshold <= 0:
			max_non_surprising += 1
		elif threshold >= 1 and total >= 3 * threshold - 2:
			max_non_surprising += 1
		elif threshold >= 2 and total >= 3 * threshold - 4:
			max_surprising += 1

	if max_surprising > num_surprising:
		max_surprising = num_surprising

	return max_surprising + max_non_surprising

for case, line in enumerate(sys.stdin):
	threshold, totals, num_surprising = parse_input(line)
	max_googlerific = max_googlerific_googlers(threshold, totals, num_surprising)
	print 'Case #%d: %d' % (case+1, max_googlerific)
