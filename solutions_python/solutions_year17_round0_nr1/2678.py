import fileinput

def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
    	s, k = next(fin).split(' ')
    	k = int(k)
    	l = [0 for i in range(len(s))]
    	for i in range(len(s)):
    		if s[i] == '-':
    			l[i] = 0
    		else:
    			l[i] = 1
    	counter = 0
    	for i in range(len(l) - k + 1):
    		if l[i] == 0:
    			counter += 1
    			for t in range(k):
    				l[i + t] = 1 - l[i + t]
    	for i in range(len(l)):
    		if l[i] == 0:
    			counter = -1
    			break
    	if counter == -1:
    		print("Case #{}: IMPOSSIBLE".format(case))
    	else:
    		print("Case #{}: {}".format(case, counter))

if __name__ == '__main__':
    main()