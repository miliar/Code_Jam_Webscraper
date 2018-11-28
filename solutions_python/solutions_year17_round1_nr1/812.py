##  Code written by: Thi Hong Ngoc Do
##  D/O/B: 06/12/1989
##  Email: dothngoc@gmail.com
##  Address: 64 Atheldene Drive, St Albans, VIC 3021, Australia
##  Phone number: +61 401 418 065
##
##  Code Jam to I/O for Women 2017
##  Date: March 11, 2017

def find_init(cake,r,c):
	init = []
	for row in range(r):
		for col in range(c):
			if cake[row][col] != '?':
				init.append([row,col])
	return init

def fill_rect(lists,col_start, col_end ,initial):

	for i in range(len(lists)):
		for j in range(col_start,col_end+1):
			lists[i][j] = initial


def cut_cake(cake,r,c):
	initials = find_init(cake,r,c)

	if len(initials) == 1:
		fill_rect(cake,0,c-1,cake[initials[0][0]][initials[0][1]])
	else:
		# first row
		empty = 0
		count = 0
		while count < len(initials):

			row = initials[count][0]
			cols = [initials[count][1]]
			count += 1
			while count < len(initials):
				if initials[count][0] == row:
					cols.append(initials[count][1])
					count += 1
				else:
					break;

			if len(cols) == 1:
				fill_rect(cake[empty:row+1],0,c-1,cake[row][initials[count-1][1]])
				if empty <= r-2:
					empty = row+1
				else:
					empty = row
			else:
				col_start = 0
				for j in range(len(cols)):
					fill_rect(cake[empty:row+1],col_start,cols[j],cake[row][cols[j]])
					col_start = cols[j]+1
				if cols[-1] < c-1:
					fill_rect(cake[empty:row+1],col_start,c-1,cake[row][cols[-1]])
				if empty <= r-2:
					empty = row+1
				else:
					empty = row

		if row < r-1:
			start = row+1
			for i in range(row+1,r):
				cake[i] = cake[row]
	return cake

############
# main #

in_file = open("A-small-attempt3.in.txt", "r")
out_file = open("A-small-attempt3.out.txt", "w+")

case_count = int(in_file.readline().strip())

case = 0
while case < case_count:
	print(case)
	str_list = in_file.readline().split()

	r = int(str_list[0])
	c = int(str_list[1])

	cake = []
	for i in range(r):
		line = in_file.readline().strip()
		row = []
		for j in range(c):
			row.append(line[j])
		cake.append(row)

	result = cut_cake(cake,r,c)

	print(result)

	out_file.write("Case #" + str(case+1) + ":\n")
	for i in range(r):
		for j in range(c):
			if j != c-1:
				out_file.write(cake[i][j])
			else:
				out_file.write(cake[i][j] + "\n")

	case += 1




in_file.close()
out_file.close()
