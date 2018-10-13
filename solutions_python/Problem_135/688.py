def solve(a, A, b, B):
	s = set(A[a-1]).intersection(set(B[b-1]))
	if len(s) == 1:
		return str(list(s)[0])
	if len(s) == 0:
		return "Volunteer cheated!"
	if len(s) > 1:
		return "Bad magician!"

def main():
	T = int(raw_input())
	for t in xrange(1, T+1):
		a = int(raw_input())
		A = [map(int, raw_input().split()) for i in xrange(4)]

		b = int(raw_input())
		B = [map(int, raw_input().split()) for i in xrange(4)]

		print "Case #{0}: {1}".format(t, solve(a, A, b, B))

if __name__ == '__main__':
	main()
