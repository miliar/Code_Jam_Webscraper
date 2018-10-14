
from jammly import Jam
import math

TEST = \
"""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1"""

class QualA(Jam):
	"""
	>>> QualA().runTest(TEST)
	Case #1: 6
	Case #2: 100
	Case #3: 4
	"""
	
	ROBOTS = "OB"
	
	def jam(self, case):
		case = case.split()[1:]
		case = zip(map(int, case[1::2]), map(self.ROBOTS.find, case[::2]))
		queue = dict(
			(r,[c[0] for c in case if c[1]==r])
			for r in range(2)
		)
		t = 0
		rp = [1,1]
		for p,r in case:
			dt = abs(p - rp[r]) + 1
			rp[r] = p
			queue[r].pop(0)
			
			r2 = 1-r
			if queue[r2]:
				dp = queue[r2][0] - rp[r2]
				rp[r2] += cmp(dp,0) * min(abs(dp), dt)
			t += dt
		return t
		
if __name__ == "__main__":
	QualA.start()
