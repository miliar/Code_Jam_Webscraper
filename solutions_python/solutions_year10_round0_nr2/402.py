import fractions
import math

def GCD(*numbers):
	numbers = list(numbers)
	a = numbers.pop(0)
	for b in numbers:
		a = fractions.gcd(a,b)
	return a

class FairWarning(object):
	
	def __init__(self, file='test.in'):
		self.next = open(file).next

	def solve(self):
		case = map(int, self.next().split())
		T = sorted(set(case[1:]), reverse=True)
		gcd = GCD(*T)
		m = GCD(*[ T[i] - T[i+1] for i in range(len(T)-1)])

		count = T[0] / m + 1

		while True:
			key = count * m - T[0]
			found = 1
			for x in T[1:]:
				bad = (key + x) % m
				if bad: break
				found += 1
			if found == len(T):
				break
			count += 1

		if GCD(*[x+key for x in T]) > gcd: return key

		return 0

	def run(self):
		n = int(self.next())

		with open('result.txt', 'w') as f:
			for i in range(n):
				result = self.solve()
				result_s = 'Case #%d: %d'%(i+1, result)
				print result_s
				f.write(result_s + '\n')

if __name__ == '__main__':
	FairWarning(file='B-large.in').run()
