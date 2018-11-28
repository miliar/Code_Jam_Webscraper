
def read_my_file(filename):
	with open(filename, 'r') as f:
		T = int(f.readline())
		output = open("B-small-attempt0.out", "w")
		for t in range(T):
			output.write("Case #%d: " % (t+1))
			print("Case #%d: " % (t+1))
			A, B, K = [int(n) for n in f.readline().split()]
			W = 0

			for a in range(A):
				for b in range(B):
					k = int(bin(a&b), 2)
					if k < K:
						W+=1
			print W
			
			output.write('%d\n' %W)
if __name__ == '__main__':
    read_my_file('B-small-attempt0.in')