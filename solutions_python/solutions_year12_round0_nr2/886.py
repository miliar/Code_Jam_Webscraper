import sys

def solve(S, p, testcase):
    googlers = 0

    for i in range(len(testcase)):
	mod = testcase[i] % 3
	div = testcase[i] / 3

	if p <= div:
	    googlers += 1
	    continue
	
	if testcase[i] != 0:
	    if mod == 1:
		if p <= div + 1:
		    googlers += 1
	    elif mod == 0:
		if p <= div:
		    googlers += 1
		elif p <= div + 1:
		    if S > 0:
			googlers += 1
			S -= 1
	    else:
		if p <= div + 1:
		    googlers += 1
		elif p <= div + 2:
		    if S > 0:
			googlers += 1
			S -= 1	    
    return googlers            

def main(input_file, out_file):
    f = open(input_file, 'r')
    g = open(out_file, 'w')
    T = int(f.readline())
    
    for i in range(T):
        testcase = f.readline().split()
        N = int(testcase[0])
        S = int(testcase[1])
        p = int(testcase[2])
        testcase = map(int,testcase[3:])        
        #print N,S,p, testcase
        sol = solve(S, p, testcase)
        print 'Case #{0}: {1}'.format(i+1, sol)
        g.write('Case #{0}: {1}\n'.format(i+1, sol))
    f.close()
    g.close()

if __name__ == "__main__":
    main('input.txt', 'output.txt')
        
    
