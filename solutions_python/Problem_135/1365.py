def main():
	cases = int(input())

	for i in range(cases):
		answer1 = input().strip()
		grid1 = []
		for j in range(4):
			grid1.append(input().split())
		answer2 = input().strip()
		grid2 = []
		for j in range(4):
			grid2.append(input().split())
		overlap = set(grid1[int(answer1)-1]).intersection(set(grid2[int(answer2)-1]))

		out = ""

		if len(overlap) == 0:
			out = "Volunteer cheated!"
		elif len(overlap) > 1:
			out = "Bad magician!"
		else:
			out = overlap.pop()

		print("Case #%d: %s" % (i+1, out))
main()