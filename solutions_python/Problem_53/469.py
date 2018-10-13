from sys import argv
def snapper(n, k):
	return ((k % 2**n)==2**n - 1)

if __name__ == '__main__':
	file = open(argv[1])
	runs = int(file.readline())
	for i in range(runs):
		string = file.readline()
		vals = string.split()
		res = 'OFF'
		if(snapper(int(vals[0]), int(vals[1]))):
			res = 'ON'
		
		print("Case #%i: %s"%(i+1, res))


