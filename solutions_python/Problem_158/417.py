mat=[[[1,0,0,0],
[1,1,0,0],
[1,0,0,0],
[1,1,0,0]],

[[1,1,0,0],
[1,1,0,0],
[1,1,1,0],
[1,1,0,0]],

[[1,0,0,0],
[1,1,1,0],
[1,0,1,0],
[1,1,1,1]],

[[1,1,0,0],
[1,1,0,0],
[1,1,1,1],
[1,1,0,1]]]



t=int(raw_input())
for case in range(t):
	x,r,c=[int(x1) for x1 in raw_input().split()]

	if mat[r-1][c-1][x-1]==1:
		print "Case #{}: {}".format(case+1,"GABRIEL")
	else:
		print "Case #{}: {}".format(case+1,"RICHARD")


		
