possible = set([
	(1,1,1),
	
	(1,2,1),
	(1,2,2),

	(1,3,1),

	(1,4,1),
	(1,4,2),

	(2,2,1),
	(2,2,2),

	(2,3,1),
	(2,3,2),
	(2,3,3),

	(2,4,1),
	(2,4,2),

	(3,3,1),

	(3,4,1),
	(3,4,2),
	(3,4,3),

	(4,4,1),
	(4,4,2),



	(3,3,3),
	(3,4,4),
	(4,4,4),
])


assert len(possible)==22

N = int(raw_input())
for i in xrange(N):
	X, R, C = map(int, raw_input().split())

	if R>C : R,C = C,R
	
	answer = "GABRIEL" if (R,C,X) in possible else "RICHARD"

	print "Case #%d: %s"%(i+1, answer)
	