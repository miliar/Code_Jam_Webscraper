import sys

i_file = open(sys.argv[1], 'r')
o_file = open('/home/neeraj/ggle/output5g.txt', 'w')

T = int(i_file.readline())
if T>100 or T<1:
	exit()

i = 1
results = []
def f (r):
	a = [int(i) for i in r.split(' ')]
	return a

while i <= T:
	i += 1
	r1 = []
	r1s = []
	r2 = []
	r2s = []
	a1 = int(i_file.readline())
	if a1 not in range(1,5):
		exit()
	r1s.append(i_file.readline())
	r1s.append(i_file.readline())
	r1s.append(i_file.readline())
	r1s.append(i_file.readline())
	a2 = int(i_file.readline())
	if a2 not in range(1,5):
		exit()
	r2s.append(i_file.readline())
	r2s.append(i_file.readline())
	r2s.append(i_file.readline())
	r2s.append(i_file.readline())

	r1 = f(r1s[a1 - 1])
	r2 = f(r2s[a2 - 1])	
	j = 0
	
	for k in r1:
		if k in r2:
			j += 1
			a1 = k
	if j == 0:
		results.append('Volunteer cheated!')
	elif j >= 2:
		results.append('Bad magician!')
	else:
		results.append(a1)

for i in range(T):
	a = 'Case #' + str(i+1) + ': ' + str(results[i]) + str('\n')
	o_file.write(a)

i_file.close()
o_file.close()

	
