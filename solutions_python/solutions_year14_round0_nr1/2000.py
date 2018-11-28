import sys

sys.stdin = open("magic_trick.in", "r")
sys.stdout = open("magic_trick.out", "w")

cases = int(raw_input())

for case in xrange(1, cases + 1):

	first_rows = []
	second_rows = []

	first_row = int(raw_input())

	for x in range(4):
		first_rows.append(raw_input().split())

	second_row = int(raw_input())

	for x in range(4):
		second_rows.append(raw_input().split())

	ans = ""

	first_row = first_rows[first_row - 1]
	second_row = second_rows[second_row - 1]

	intersection = [val for val in first_row if val in second_row]

	if len(intersection) is 0:
		ans = "Volunteer cheated!"
	elif len(intersection) is 1:
		ans = str(intersection[0])
	else:
		ans = "Bad magician!"

	print "Case #%d: %s" % (case, ans)