

def flip(n, k):
	t = n
	flipper = pow(2,k)-1

	flips = 0

	for i in range(0,len(str(bin(t))[2:]) - (k-1)):
		if t / pow(2,i) % 2 == 1:
			t ^= (flipper << i)
			flips += 1

	if t == 0:
		return flips
	else:
		return -1


def parse(line):
	l = line.split(' ')

	n = int(l[0].replace('-','1').replace('+','0'), 2)
	k = int(l[1])

	return (n,k)


lines = int(raw_input())

for i in range(lines):
	n, k = parse(raw_input())

	f = flip(n,k)

	print('Case #' + str(i+1) + ': ' + ('IMPOSSIBLE' if f == -1 else str(f)))
