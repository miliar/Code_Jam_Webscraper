import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >=2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    no_cases = int(f.readline())
    for case in xrange(no_cases):
    	row_list = []
    	for ques in range(2):
    		ans = int(f.readline())
    		for i in xrange(ans):
    			row = f.readline()
    		row_list.append([int(i) for i in row.split()])
    		for i in xrange(4 - ans):
    			row = f.readline()
    	intersection = set(row_list[0]) & set(row_list[1])
    	match = len(intersection)
    	if match == 0:
    		result = "Volunteer cheated!"
    	elif match == 1:
    		result = str(list(intersection)[0])
    	else:
    		result = "Bad magician!"
    	print "Case #%d: %s" % (case + 1, result)