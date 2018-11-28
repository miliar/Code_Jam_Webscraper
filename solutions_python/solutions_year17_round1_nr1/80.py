t = int(input())  # read a line with a single integer

for j in range(1, t + 1):
    r, c = map(int, input().split(" "))

    last_line = ['?']*c
    empty_lines = 0
    print("Case #{}:".format(j))

    for i in range(r):
    	line = list(input())
    	if all([i == '?' for i in line]):
    		line = last_line
    		empty_lines += 1

    	else:
    		j = 0
    		while line[j] == '?':
    			j += 1

    		line[:j] = line[j] * j
    		j += 1

	    	while j < c:
	    		if line[j] == '?':
	    			line[j] = line[j-1]
	    		j += 1


	    	last_line = line

	    	for i in range(empty_lines+1):
	    		print(''.join(last_line))

	    	empty_lines = 0



    for i in range(empty_lines):
    	print(''.join(last_line))