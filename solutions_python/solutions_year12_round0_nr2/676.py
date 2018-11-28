ll = open('/Users/pittaya/Downloads/B-large.in').readlines()
# ll = open('/Users/pittaya/tmp/dance.in').readlines()
numcase = ll[0]

def possible_scores(sum_score):
	m = sum_score % 3
	s = sum_score/3
	if m == 1:
		return ([s, s, s+1], m)
	elif m == 2:
		return ([s, s+1, s+1], m)
	else:
		return ([s, s, s], m)

i = 1
for l in ll[1:]:
	l = l.strip()
	(n, s, p, t) = l.split(' ', 3)
	s = int(s)
	p = int(p)
	tt = t.split(' ')
	ok = 0
	# print "at least %d / surprise = %d" % (p, s)
	for score in tt:
		(ps, mod) = possible_scores(int(score))
		if (ps[0] >= p) or (ps[1] >= p) or (ps[2] >= p):
			# print "%s : %s" % (score, ps)
			ok += 1
		elif (p - max(ps) == 1) and (s > 0) and mod != 1:
			if sum(ps) > 1:
				# print "%s : %s (*)" % (score, ps)
				ok += 1
				s -= 1
			else:
				# print "%s : - %s" % (score, ps)
				pass
		else:
			# print "%s : -- %s" % (score, ps)
			pass
	
	print 'Case #%d: %d' % (i, ok)
	i += 1