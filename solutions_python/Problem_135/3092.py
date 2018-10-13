import sys
t = int(sys.stdin.readline())
for i in range(t):
	a = int(sys.stdin.readline())
	mat1, mat2 = [0, 0, 0, 0], [0,0,0,0]
	for k in range(4):
		mat1[k] = sys.stdin.readline().split()
	b = int(sys.stdin.readline())
	for k in range(4):
		mat2[k] = sys.stdin.readline().split()
	s2 = set(mat2[b-1])
	intersection = [v for v in mat1[a-1] if v in s2]
	if len(intersection) == 0:
	 	print("Case #"+str(i+1)+": Volunteer cheated!")
	elif len(intersection) == 1:
		print("Case #"+str(i+1)+": "+intersection[0])
	else: 
	 	print("Case #"+str(i+1)+": Bad magician!")
