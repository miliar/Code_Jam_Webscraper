numcases = int(input())
for ncase in range(1, numcases+1):
	line	= input().split()
	N		= int(line[0])
	M		= int(line[1])
	numbers	= []
	rowtable = []
#	clmtable = []
#	for n in range(N):
#		rowtable.append([])
#	for n in range(M):
#		clmtable.append([])
	for r in range(N):
		rowtable.append([])
		line = input().split()
		for c in line:
			num = int(c)
			rowtable[r].append(num)
			if num not in numbers:
				numbers.append(num)
	numbers.sort()
#			clmtable[c].append(num)
#	for n in range(M):
#		clmtable[n].append(n) 
#	for r in rowtable:
#		print(r)
#	print()
#	# sort
#	rowtable.sort()
#	clmtable.sort()
#	table = []
#	for r in range(N):
#		table.append([])
#		for c in range(M):
#			table[r].append(rowtable[r][clmtable[c][N]])
#	deleted = True
	totalnum = N*M
#	for r in table:
#		print(r)
	for cstart in numbers:
		deleted = True
		# row deleting
		length = len(rowtable)
		for r in range(length-1, -1, -1):
			same = True
			for i in rowtable[r]:
				if cstart != i:
					same = False
					break
			if same:
				totalnum -= len(rowtable[r])
				rowtable.pop(r)
				deleted = True
				if totalnum == 0:
					break
		if totalnum == 0:
			break
		# column deleting
		length = len(rowtable[0])
		for c in range(length-1, -1, -1):
			same = True
			for r in range(len(rowtable)):
				if cstart != rowtable[r][c]:
					same = False
					break
			if same:
				totalnum -= len(rowtable)
				for r in range(len(rowtable)):
					rowtable[r].pop(c)
				deleted = True
				if totalnum == 0:
					break
		if totalnum == 0 or not deleted:
			break

		
#	while totalnum != 0 and deleted:
#		deleted = False
#		while totalnum != 0 and table[0][0] == table[0][-1]:
#			same = True
#			cstart = table[0][0]
#			for c in table[0]:
#				if cstart != c:
#					same = False
#			if same:
#				totalnum -= len(table[0])
#				table.pop(0)
#				deleted = True
#		for r in table:
#			print(r)
#		print(table)
#		while totalnum != 0 and table[0][0] == table[-1][0]:
#			same = True
#			cstart = table[0][0]
#			for r in range(len(table)):
#				if table[r][0] != cstart:
#					same = False
#			if same:
#				totalnum -= len(table)
#				for r in range(len(table)):
#					table[r].pop(0)
#				deleted = True
#		for r in table:
#			print(r)
#		print(table)
	print("Case #%d: " % ncase, end="")
	if totalnum == 0:
		print("YES")
	else:
		print("NO")

#	for row in table:
#		for num in row:
#			print("%d " % num , end="")
#		print("")
#	print("")
