t = int(input())
for t_index in range(t):
	r,c = input().split()
	r = int(r)
	c = int(c)
	lines = []
	for l in range(r):
		l = list(input())
		lines.append(l)
		last_char = '?'
		for i in range(len(l)):
			if l[i] == '?':
				l[i] = last_char
			else:
				last_char = l[i]
		last_char = '?'
		for i in range(len(l)-1,-1,-1):
			if l[i] == '?':
				l[i] = last_char
			else:
				last_char = l[i]
	last_line = ["?"]*c
	for i in range(len(lines)):
		if "?" in lines[i]:
			lines[i] = last_line
		else:
			last_line = lines[i]
	last_line = ["?"]*c
	for i in range(len(lines)-1,-1,-1):
		if "?" in lines[i]:
			lines[i] = last_line
		else:
			last_line = lines[i]
	print("Case #"+str(t_index+1)+":")
	for l in lines:
		print("".join(l))
