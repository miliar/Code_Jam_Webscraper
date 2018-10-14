# Task А
import fileinput

def check(m):
	s = 0
	k = 0
	for n in m:
		if s < k:
			return False
		s = s + n
		k = k + 1
	return True

def add_friend(m):
	k = 0
	while k < len(m):
		if m[k] < 9:
			m[k] = m[k] + 1
			return
		k = k + 1

stdin = fileinput.input()
T = int(stdin.readline())
for ti in range(T):
	line = stdin.readline().strip().split(' ')
	Smax = int(line[0])
	m = []
	for li in line[1]:
		m.append(int(li))

	friends = 0
	while (check(m) == False):
		add_friend(m)
		friends = friends + 1
	print('Case #' + str(ti + 1) + ': ' + str(friends))
