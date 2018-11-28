import sys

def recycle(n):
    lst = []
    s = str(n)
    for i in range(len(s)):
	lst.append(int(s[i:]+s[:i]))
    return lst

def solve(A,B):
    count = 0
    if A/10 == 0 and B/10 == 0:
	return 0
    ndig = len(str(A))
    for i in range(A,B):
	for k in range(ndig-1):
	    lastdig = i % (10 ** (k+1))
	    if lastdig >= (10 ** k) and lastdig <= B/(10**(ndig - k - 1)):
		rec = lastdig * (10 ** (ndig - k - 1)) + i/(10 ** (k+1))
		if rec <= B and rec > i:
		    count += 1
		    #print '({0} < {1})'.format(i,rec)
    return count             

def main(input_file, out_file):
    f = open(input_file, 'r')
    g = open(out_file, 'w')
    T = int(f.readline())
    
    for i in range(T):
	testcase = f.readline().split()
        A = int(testcase[0])
        B = int(testcase[1])

        sol = solve(A,B)
        print 'Case #{0}: {1}'.format(i+1, sol)
        g.write('Case #{0}: {1}\n'.format(i+1, sol))
    f.close()
    g.close()

if __name__ == "__main__":
    main('input.txt', 'output.txt')
        
    
