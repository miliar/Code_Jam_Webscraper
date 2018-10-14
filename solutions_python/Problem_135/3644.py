import math

input = open('input1a.in', 'r')
output = open('input1a.out', 'w');

cases = int(input.readline())
print cases
i = 0
while i < cases:
	r1 = int(input.readline())
	b1 = []

	print 'Do1'

	for j in range(4):
		line = input.readline()
		line = line.rstrip().split(' ')
		b1.append(line)

	print 'Do2'

	r2 = int(input.readline())
	b2 = []
	for j in range(4):
		line = input.readline()
		line = line.rstrip().split(' ')
		b2.append(line)

	comp1 = b1[r1-1]
	comp2 = b2[r2-1]
	print comp1
	print comp2

	print 'Do3'

	k = 0
	r = 0
	for j in range(4):
		for l in range(4):
			if int(comp1[j])==int(comp2[l]):
				k = k + 1
				print k
				r = comp1[j]
				print r

	print 'Do'

	if k == 0:
		print 'k0'
		output.write("Case #"+str(i+1)+": Volunteer cheated!\n")
	else:
		if k == 1:
			print 'k1'
			output.write("Case #"+str(i+1)+": "+r+"\n")
		else:
			output.write("Case #"+str(i+1)+": Bad magician!\n")

	i = i + 1

output.close()
