import math
def main():
	case = int(raw_input())
	for case_loop in range(0, case):
		n = int(raw_input())
		line_a_str = raw_input().split(' ')
		line_b_str = raw_input().split(' ')
		a = [int(i) for i in line_a_str]
		b = [int(i) for i in line_b_str]
		a.sort()
		b.sort()
		b.reverse()
		sum = 0
		for n_loop in range(0, n):
			sum += a[n_loop] * b[n_loop]
		print "Case #%s: %s" % (case_loop + 1, sum)


if __name__=="__main__":
	main()
