
from jammly import Jam, multiline
import math

TEST = \
"""3
2
2 1
3
1 3 2
4
2 1 4 3"""

class QualD(Jam):
	"""
	>>> QualD().runTest(TEST)
	Case #1: 2.000000
	Case #2: 2.000000
	Case #3: 4.000000
	"""
	
	cases = multiline(2)
	
	def jam(self, N, array):
		N = int(N)
		array = map(int, array.split())
		arrays = zip(array, sorted(array))
		return N - len([a for a,b in arrays if a == b])
		
if __name__ == "__main__":
	QualD.start()
