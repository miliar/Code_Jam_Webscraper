input_file = open("B-small-attempt0.in","r");
output_file = open("B-small-attempt1.out","a");
m = input_file.readline()


for k in range(int(m)):
#	l = [int(i) for i in raw_input().split()]
	l = [int(i) for i in input_file.readline().split()]
	k1 = range(l[0])
	k2 = range(l[1])
	l3 = []
	l2 = []
	count = 0
	for i in k1:
		for j in k2:
			l2.append((i,j))
	for n in l2:
		l3.append(n[0] & n[1])
	for num in l3:
		if num < l[2]:
			count = count + 1
	output_file.write("Case #" + str(k+1) + ": " + str(count))  
	output_file.write('\n')
