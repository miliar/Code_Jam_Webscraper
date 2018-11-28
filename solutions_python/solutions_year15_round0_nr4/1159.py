index = 1
d = {}
d[2] = [[1,2],[1,4],[2,3],[2,4],[2,2],[3,4],[4,4]]
d[3] = [[2,3],[3,3],[3,4]]
d[4] = [[3,4],[4,4]]
for i in range(input()):
	x,r,c = map(int,raw_input().split())
	if x==1:answer  = "GABRIEL"
	elif [r,c] in d[x] or [c,r] in d[x]:
		answer  = "GABRIEL"
	else:
		answer  = "RICHARD"
	print "Case #"+str(index)+": "+answer
	index += 1


