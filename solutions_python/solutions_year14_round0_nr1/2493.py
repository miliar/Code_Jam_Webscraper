#! python2
import sys

sys.stdin = open('real.in')
sys.stdout = open('real.out', 'w')

n = int(raw_input())

for i in range(n):
	a = int(raw_input())
	rowsa = [
		[x for x in raw_input().split(' ')]
		for j in range(4)
	]
	b = int(raw_input())
	rowsb = [
		[x for x in raw_input().split(' ')]
		for j in range(4)
	]

	matches = set(rowsa[a - 1]) & set(rowsb[b - 1])

	if len(matches) == 1:
		res = list(matches)[0]
	elif len(matches) == 0:
		res = "Volunteer cheated!"
	else:
		res = "Bad magician!"


	print "Case #{}: {}".format(i+1, res)
