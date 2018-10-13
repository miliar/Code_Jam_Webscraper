intervals = [23, 90, 40, 0, 100, 9]

def solution(intervals):
	amount = sum(max(intervals[i] - intervals[i+1], 0) for i in range(len(intervals) - 1))
	rate = max(intervals[i] - intervals[i+1] for i in range(len(intervals) - 1))
	amount2 = sum( min(intervals[i], rate) for i in range(len(intervals) -  1))
	return amount, amount2


f = open("A-large.in", "r")
out = open("out.out", "w")
ntests = int(f.readline())
for i in range(ntests):
	if i > 0:
		out.write("\n")
	nintervals = int(f.readline())
	intervals = [int(n) for n in f.readline().split()]
	n1, n2 = solution(intervals)
	out.write("Case #" + str(i + 1) + ": " + str(n1) + " " + str(n2)) 