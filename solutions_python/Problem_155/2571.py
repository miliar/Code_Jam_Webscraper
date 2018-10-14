import sys

t = int(sys.stdin.readline().rstrip())

for case in range (1, t+1):
	inp = sys.stdin.readline().rstrip()
	max = int(inp.split(" ")[0])
	tail = inp.split(" ")[1]

	standing = 0
	s = 0
	more = 0
	
	while s <= max:
		standing += int(tail[s])
		s = s+1
		while standing < s:
			more = more+1
			standing = standing+1

	print("Case #"+str(case)+": "+str(more))