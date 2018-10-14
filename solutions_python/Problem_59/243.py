cases = int(raw_input())

for i in range(cases):
	
	string = raw_input()
	n = int(string.strip().split()[0])
	m = int(string.strip().split()[1])
	
	#input directories
	i_l = []
	for i1 in range(n):
		string = raw_input()
		i_l.append(string.strip())
	
	#new dirs
	i_o = []
	for i2 in range(m):
		string = raw_input()
		parts = string.strip().split('/')
		path = ""
		for i3 in range(len(parts)-1):
			path = path + '/'+str(parts[i3+1])
			i_o.append(path)
	
	print "Case #%d: %d" %(i+1, len(set(i_o) - set(i_l)))			
