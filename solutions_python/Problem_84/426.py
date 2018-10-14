
from jammly import Jam
import math

TEST = \
"""3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##.."""

class R1CA(Jam):
	r"""
	>>> R1CA().runTest(TEST)
	Case #1:
	Impossible
	Case #2:
	.
	Case #3:
	./\..
	.\//\
	./\\/
	.\/..
	"""
	
	ROBOTS = "OB"
	
	def jam(self, R, C, m):
		possible = True
		for i in range(R):
			for j in range(C):
				if m[i][j] == '#':
					if i + 1 < R and j + 1 < C \
							and m[i][j+1] == '#':
						m[i][j] = '/'
						m[i][j+1] = '\\'
						m[i+1][j] = '\\'
						m[i+1][j+1] = '/'
					else:
						possible = False
						break
		
		return "\n" + "\n".join("".join(s) for s in m) if possible \
			else "\nImpossible"
	
	@staticmethod
	def cases(file, N):
		while N:
			header = file.next()
			R,C = map(int, header.split())
			rows = [list(file.next().strip()) for i in range(R)]
			yield (R,C,rows)


if __name__ == "__main__":
	R1CA.start()
