in_f = open('B-large.in', 'r')
out_f = open('output1.txt', 'w')

line_count = 0
for line in in_f:
	count = 0
	if line_count == 0:
		line_count += 1
		continue
	line = list(str(int(line)))
	left = 0
	while left < len(line)-1:
		if line[left]<=line[left+1]:
			left += 1
		else:
			break

	if len(line) == 1 or left == len(line)-1:
		ans = 'Case #{}: {}\n'.format(line_count, ''.join(line))
		out_f.write(ans)
		line_count += 1
		continue

	while left>0 and line[left] == line[left-1]:
		left -= 1
	rest = ['9']*(len(line)-left-1)
	if line[left]>'1' or left>0:
		line[left] = str(int(line[left])-1)
		line = line[:left+1]+rest
	else:
		line = rest
	
	
	ans = 'Case #{}: {}\n'.format(line_count, ''.join(line))
	out_f.write(ans)
	line_count += 1
