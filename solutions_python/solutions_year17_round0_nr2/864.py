def last_tidy(n):
	
	strn = str(n)
	dign = [int(x) for x in strn]
	
	for i in range(1, len(dign)):
		if dign[i] >= dign[i-1]:
			continue
		else:
			for j_right in range(i, len(dign)):
				dign[j_right] = 9
			
			j_left = i-1
			while j_left > 0 and dign[j_left] == dign[j_left-1]:
				dign[j_left] = 9
				j_left -= 1
			dign[j_left] -= 1

			break


	n = "".join([str(dig) for dig in dign])
	if n[0] == "0" and len(n) > 1:
		n = n[1:]

	return n

case_count = int(input())

for case in range(case_count):
	
	n = int(input())
	
	print("Case #{0}: {1}".format(case+1, last_tidy(n)))
