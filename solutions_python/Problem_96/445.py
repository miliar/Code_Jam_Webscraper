def best_result_normal(total):
	return (total + 2) / 3

def best_result_surprising(total):
	if total == 0:
		return 0
	if total % 3 == 2:
		return total / 3 + 2
	return total / 3 + 1

cases = int(raw_input())
for case in xrange(1, cases + 1):
	info = map(int, raw_input().split())
	n, s, p, totals = info[0], info[1], info[2], info[3:]
	not_surprising = sum(1 for total in totals if best_result_normal(total) >= p)
	surprising = sum(1 for total in totals if best_result_normal(total) < p and best_result_surprising(total) >= p)
	print 'Case #%d: %s' % (case, not_surprising + min(s, surprising))