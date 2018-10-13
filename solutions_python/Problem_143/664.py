def solve(i, line):
    #print line
    a, b, k = line[0], line[1], line[2]
    aa = range(a)
    bb = range(b)
    #kk = range(k)
    retval = 0
    for xa in aa:
    	for xb in bb:
    		t = xa & xb
    		if t < k:
    			retval += 1

    return retval


if __name__ == '__main__':
    n_test = int(raw_input())
    tests = []
    #print n_test
    for i in xrange(n_test): 
        inputt = raw_input()
        a, b, k= inputt.split()
        tests.extend([[int(a), int(b), int(k)]])
    
    for i in xrange(n_test):
        print "Case #"+str(i+1)+": "+ str(solve(i, tests[i]))