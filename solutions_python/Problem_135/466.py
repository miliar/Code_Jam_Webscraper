#! /usr/bin/python

def solve(ans1, arr1, ans2, arr2):
	row1 = set(arr1[ans1])
	row2 = set(arr2[ans2])

	p = row1.intersection(row2)

	if len(p) == 1:
		return list(p)[0]

	if len(p) == 0:
		return "Volunteer cheated!"

	return "Bad magician!"


def main():
	T = int(raw_input())
	for t in xrange(T):
		ans1 = int(raw_input()) - 1
		arr1 = [raw_input().split() for i in xrange(4)]
		ans2 = int(raw_input()) - 1
		arr2 = [raw_input().split() for i in xrange(4)]
		print "Case #%d: %s" % (t + 1, solve(ans1, arr1, ans2, arr2))

if __name__ == "__main__":
	main()