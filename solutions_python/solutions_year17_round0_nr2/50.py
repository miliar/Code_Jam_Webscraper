import sys
import itertools

#filename = "test.in"
filename = None

def solve(n):
	d = map(int, list(str(n)))
	l = len(d)

	for i in range(0, l-1):
		current, nex = d[i], d[i+1]
		if current > nex:
			d[i] = d[i]-1
			j = i-1

			while(j >= 0 and d[j] > d[j+1]) :
				d[j+1] = 9
				d[j] -= 1
				j-=1
			d[i+1:] = [9] * len(d[i+1:])

	return int("".join(map(str,d)))

def main():
	if filename:
		file = open(filename)
	else:
		file = sys.stdin


	T = int(file.readline().strip())
	for i in range(T):	
		d = int(file.readline().strip())
		
		answer = solve(d)
		print "Case #%d: %d" % (i+1, answer)
		

	if file is not sys.stdin:
	    file.close()


if __name__ == '__main__':
	main()
	
