def process(n, k):
	a = []
	for i in xrange(n):
		a.append(False)
	
	for i in xrange(k):
		j = 0
		while (j < n and a[j]):
			a[j] = False
			j += 1
		if j < n:
			a[j] = True
		
	light = True
	for i in a:
		if not i:
			return False
			
	return True
		

def main():
	file = open("in.txt", "r")
	file_out = open("out.txt", "w")
	lines = int(file.readline())
	for i in xrange(lines):
		line = file.readline()
		n, k = [int(s) for s in line.split()]
		light = process(n,k)
		file_out.write("Case #%s: %s\n" % (i + 1, ['OFF', 'ON'][light]))
	file.close()
	file_out.close()
	
if __name__ == "__main__":
	main()