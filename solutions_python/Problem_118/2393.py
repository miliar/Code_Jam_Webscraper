
import math

def palindrom(x):
	y = x;
	reverse = 0;
	while (x > 0):
		reverse = reverse*10 + x % 10;
		x = x/10;
	return reverse == y

def main():
	f = open("file.in", "r")
	tests = int(f.readline())
	for t in xrange(tests):
		cnt = 0
		a, b = f.readline().split()
		a = int(math.ceil(int(a)**0.5))
		b = int(math.floor(int(b)**0.5))
		for i in xrange(b - a + 1):
			tmp = a + i
			if (palindrom(tmp) == True):
				if (palindrom (tmp**2) == True):
					cnt += 1
		print "Case #" + str(t+1) + ": " + str(cnt)

if __name__ == "__main__":
	main()
