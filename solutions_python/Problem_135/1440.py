#python3
#actually, it's twice row, not row/col
# I wasn't feeling imaginitive with variable names

for N in range(int(input())):
	rownum = int(input())
	for i in range(1, 5):
		buf = input()
		if i == rownum:
			row = set([int(x) for x in buf.split()])
	colnum = int(input())
	col = set()
	for i in range(1, 5):
		buf = input()
		if i == colnum:
			col = set([int(x) for x in buf.split()])
	both = row.intersection(col)
	print("Case #%d: " % (N+1), end="")
	if len(both) == 0:
		print("Volunteer cheated!")
	elif len(both) == 1:
		print(both.pop())
	else:
		print("Bad magician!")
