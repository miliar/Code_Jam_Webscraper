
data = open('C-large.in', 'r').readlines()
t = int(data[0])
answ = []

# 0...1....0 | 0 1 8 4
# 0.2.1.2..0 | 1 1 4 3
# 03231323.0 | 3 1 2 1
# 0323132340 | 1 7 1 ?
def stall(odd, even, ln, k):
	if k <= even + odd:
		if ln % 2 == 0:
			if k <= even:
				return ln // 2, ln // 2 - 1
			return (ln - 1) // 2, (ln - 1) // 2
		else:
			if k <= odd:
				return (ln - 1) // 2, (ln - 1) // 2
			return ln // 2, ln // 2 - 1
	k -= odd + even
	if (ln - 1) // 2 % 2 == 1:
		return stall(odd*2+even, even, ln // 2, k)
	else:
		return stall(even, even+odd*2, ln // 2, k)

for i in range(t):
	n, k = data[i + 1].split()
	n, k = int(n), int(k)
	if n % 2 == 0:
		x, y = stall(0, 1, n, k)
	else:
		x, y = stall(1, 0, n, k)
	answ.append('{} {}'.format(x, y))

with open('C-large.out', 'w') as f:
    for i, o in enumerate(answ):
        f.write('Case #{}: {}\n'.format(i+1, o))
