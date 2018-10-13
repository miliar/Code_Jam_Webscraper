def parse_param():
    raw_input()
    return map(int , raw_input().split())

def solve(l):
    sorted = l[:]
    sorted.sort()
    count = 0
    for i in range(len(sorted)):
	if l[i] != sorted[i]:
	    count += 1
    return float(count)

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
	print "Case #%d:" % i,
	l = parse_param()
	print "%.6f" % solve(l)

main()

