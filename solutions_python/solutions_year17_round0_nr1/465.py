t = int(raw_input()) 
for i in xrange(1, t + 1):
    data, flip_size = [s for s in raw_input().split(" ")]
    mod_data = [elem == '+' for elem in data]
    flip_size = int(flip_size)
    count = 0
    for ii, elem in enumerate(mod_data):
    	if elem:
    	    continue
    	if ii + flip_size > len(data):
    		break
    	count += 1
    	for j in range(flip_size):
    		mod_data[ii + j] = 1 - mod_data[ii + j]
    if sum(mod_data) < len(mod_data):
    	print "Case #{}: IMPOSSIBLE".format(i)
    else:
        print "Case #{}: {}".format(i, count)