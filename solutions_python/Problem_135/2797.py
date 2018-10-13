from sys import argv

with open(argv[1]) as f:
	d = f.readlines()

numTry = int(d[0].strip())
del d[0]

for i in range(numTry):
	pos1 = int(d[0].strip())
	mat1 = []
	mat1.append(d[1].strip().split(' '))
	mat1.append(d[2].strip().split(' '))
	mat1.append(d[3].strip().split(' '))
	mat1.append(d[4].strip().split(' '))
	pos2 = int(d[5].strip())
	mat2 = []
	mat2.append(d[6].strip().split(' '))
	mat2.append(d[7].strip().split(' '))
	mat2.append(d[8].strip().split(' '))
	mat2.append(d[9].strip().split(' '))
	d = d[10:]
	available = []
	for x in mat1[pos1-1]:
		#print(x)
		if x in mat2[pos2-1]:
			available.append(x)

	if len(available) == 1:
		print('Case #{}:'.format(i+1),available[0])
	elif len(available) == 0:
		print('Case #{}:'.format(i+1),"Volunteer cheated!")
	if len(available) > 1:
		print('Case #{}:'.format(i+1),"Bad magician!")