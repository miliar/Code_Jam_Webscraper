#!python

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	t = int(f.readline())
	for i in range(1, t+1):
		w.write("Case #%d: " % i)
		a, b, k = [int(x) for x in f.readline().split()]
		q = 0
		for i in range(a):
			for j in range(b):
				if i & j < k:
					q += 1
		w.write("%d\n" % q)

if __name__ == "__main__":
	main()