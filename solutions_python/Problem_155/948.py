"""
Codejam 2015
"""
import sys

T = int(raw_input())
CASES = []

for i in xrange(T):
	a = raw_input().split()
	CASES.append((int(a[0]), a[1]))


FRIENDS = []
for case in CASES:
	Smax = case[0]
	friend_count = 0
	current_count = 0

	print >> sys.stderr,  ">>%s"%(i,)
	for i in xrange(len(case[1])):
		si = int(case[1][i])

		if current_count < i:
			friend_count += i - current_count
			current_count += i - current_count

		current_count += si

		print >> sys.stderr, friend_count
		print >> sys.stderr, current_count
	FRIENDS.append(friend_count)

for i in xrange(T):
	print "Case #%s: %s" % (i+1, FRIENDS[i])

