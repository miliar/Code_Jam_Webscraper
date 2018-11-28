import sys

def is_pow2(n):
	return (q & (q - 1) == 0)

def get_int_log2(n):
	int_log2 = 0
	while (n != 1):
		int_log2 += 1
		n >>= 1
	return int_log2
	
def get_gcd(a, b):
	if (b == 0):
		return a
	else:
		return get_gcd(b, a % b)

input = open(sys.argv[1], 'r')

t = int(input.readline())

for case in range(1, t + 1):

	[p, q] = map(int, input.readline().split('/'))
	
	gcd = get_gcd(p, q)
	p /= gcd
	q /= gcd
	
	possible = False
	denominators = []
	while (True):
		if (not is_pow2(q)):
			break
		elif (p == 1):
			possible = True
			denominators.append(q)
			break
		else:
			denominator = 2
			while ((1.0 / denominator) >= (float(p) / float(q))):
				denominator *= 2
			factor = q / denominator
			denominators.append(denominator)
			p -= factor

	sys.stdout.write('Case #' + str(case) + ': ')

	if (not possible):
		sys.stdout.write('impossible')
	else:
		elf_generations = get_int_log2(min(denominators))
		sys.stdout.write(str(elf_generations))

	if (case < t):
		print('')

input.close()
