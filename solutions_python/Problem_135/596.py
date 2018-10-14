from sys import stdin

def main():
	T = int(stdin.readline())
	for t in xrange(1,T+1):
		r1 = int(stdin.readline())
		for i in xrange(1,r1):
			stdin.readline()
		s1 = {int(x) for x in stdin.readline().strip().split(" ")}
		for i in xrange(r1+1,5):
			stdin.readline()
		r2 = int(stdin.readline())
		for i in xrange(1,r2):
			stdin.readline()
		s2 = {int(x) for x in stdin.readline().strip().split(" ")}
		for i in xrange(r2+1,5):
			stdin.readline()
		s = s1&s2
		if len(s) == 0:
			result = "Volunteer cheated!"
		elif len(s) > 1:
			result = "Bad magician!"
		else:
			result = str(s.pop())
		print "Case #%d:"%t, result

if __name__ == "__main__":
	main()