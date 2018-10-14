def half(content, arr):
	# print content
	i = 0
	row1 = int(content[i])
	i += 1
	for j in range(i, i+4):
		a = []
		s = content[j].split(" ")
		for c in range(0, len(s)):
			a.append(int(s[c]))

		arr.append(a)
	return arr[row1-1]

def test(content, t):
	arr1 = []
	j = 0
	row1 = half(content[j:j+5], arr1)

	j += 5

	arr2 = []
	
	row2 = half(content[j:j+5], arr2)

	suc = 0
	num = 0
	for i in row1:
		if i in row2:
			num = i
			suc += 1


	msg = ''
	if suc == 0:
		msg = "Volunteer cheated!"
	elif suc == 1:
		msg = str(num)
	else:
		msg = "Bad magician!"

	print 'Case #{0}: {1}'.format(t, msg)

f = open("input.txt")
c = f.readlines()

tests = c[0]
i = 1
for t in range(1, int(tests)+1):
	con = c[i:i+10]
	test(con, t)
	i += 10





