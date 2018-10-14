import fileinput

ct = 1
for line in fileinput.input():
	l = line.split()
	if len(l) == 1:
		continue
	input_str = l[1]
	invite = 0
	clapping = 0
	for idx in range(len(input_str)):
		while clapping < idx and idx != 0:
			invite+=1
			clapping+=1
		clapping += int(input_str[idx])
	print("Case #%d: %d" % (ct,invite))
	ct +=1