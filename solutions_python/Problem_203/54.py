T = int(input())

def fill_row(row):
	# print(row)
	first_element = [i for i in row if i != "?"][0]
	new_row = list()
	last_elem = '?'
	for i in row:
		if i == '?':
			if last_elem == '?':
				new_row.append(first_element)
			else:
				new_row.append(last_elem)
		else:
			new_row.append(i)
			last_elem = i

	return(new_row)

for i in range(T):


	print("Case #" + str(i+1) + ":")



	R,C = map(int, input().split(" "))

	rows = list()
	# first non empty row
	first_row = list()

	for j in range(R):
		r = list(input())
		rows.append(r)
		if len(first_row) == 0 and (len(set(r)) > 1 or '?' not in r):
			first_row = fill_row(r)

	last_row = list()
	for row in rows:
		if len(set(row)) == 1 and '?' in row:
			# Empty
			if len(last_row) > 0:
				print("".join(last_row))
			else:
				print("".join(first_row))
		else:
			# Non empty
			last_row = fill_row(row)
			print("".join(last_row))



