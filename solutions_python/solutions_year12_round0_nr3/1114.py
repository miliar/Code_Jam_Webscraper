import sys
f = open(sys.argv[1], 'r')
n = f.readline()
in_put = f.readlines()

def compute(two_number):
	two_number = two_number.split(' ')
	two_number = map(int, two_number)
	m = []
	for i in range(two_number[0], two_number[1] + 1 ):
		i_str = str(i)
		i_conca = i_str + i_str
		for j in range(0, len(i_str)):
			a = i_conca[j: (j + len(i_str))]
			if int(a) > i and int(a) <= two_number[1]:
				if [i,a] not in m:
					m.append([i,a])
	return len(m)
	
for i in range(0, len(in_put)):
	to_return = compute(in_put[i])
	print "Case #" + str(i + 1) +": " + str(to_return)
