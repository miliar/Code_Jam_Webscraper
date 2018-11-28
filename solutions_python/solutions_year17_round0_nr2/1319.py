
ans = []

with open("B-large.in") as f:
    content = f.readlines()

content = [x.strip() for x in content]
t = int(content[0])

for i in range(t):
	n = content[i+1]
	digits = list(map(int, n))
	dec_flag = False
	idx = 0
	change_flag = False
	frequency = 1

	for j in range(1, len(digits)):
		if digits[j] < digits[j-1]:
			idx = j - frequency + 1
			change_flag = True
			break

		if j != 0 and digits[j] == digits[j-1]:
			frequency += 1
		else:
			frequency = 1

	if change_flag:
		for j in range(idx, len(digits)):
			digits[j] = 9
		digits[idx-1] -= 1

	ans.append(''.join(map(str, digits)))

fw = open("B-large.out", 'w')

for i, x in enumerate(ans):
	fw.write("Case #{0}: {1}\n".format(i+1, str(x).lstrip('0')))





