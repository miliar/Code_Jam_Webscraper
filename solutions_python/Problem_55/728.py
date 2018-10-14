#!/usr/bin/python

def main():
	file_in = open("in.txt", "r")
	file_out = open("out.txt", "w")
	tests = int(file_in.readline())
	for case in xrange(tests):
		runs, capacity = [int(i) for i in file_in.readline().split()][:2]
		l = [int(i) for i in file_in.readline().split()]
	
		profit = 0
		for run in xrange(runs):
			n = 0
			p = 0
			while n + l[0] <= capacity and p < len(l):
				n += l[0]
				l.append(l.pop(0))
				p += 1
			profit += n
			
		file_out.write("Case #%d: %d\n" % (case + 1, profit))
			
	
	file_in.close()
	file_out.close()
	
if __name__ == "__main__":
	main()