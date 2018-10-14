T = int(raw_input())
fileobj = open("1_op.txt","w")
for t in range(1,T+1):

	N = int(raw_input())
	res = 0
	points = []
	for i in range(N):
		inp = raw_input().split(' ')
		curr_point=[ int(inp[0]) , int(inp[1]) ]
		for j in points:
			if ((j[0]>curr_point[0]) and (j[1] < curr_point[1])) or ((j[0]<curr_point[0]) and (j[1] > curr_point[1])):
				res = res+1
		points.append(curr_point)
	fileobj.write( "Case #"+str(t)+": "+str(res)+"\n")
fileobj.close()
	
