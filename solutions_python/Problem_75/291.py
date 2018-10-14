
from jammly import Jam, multiline
import math

TEST = \
"""5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW"""

class QualB(Jam):
	"""
	>>> QualB().runTest(TEST)
	Case #1: [E, A]
	Case #2: [R, I, R]
	Case #3: [F, D, T]
	Case #4: [Z, E, R, A]
	Case #5: []
	"""
		
	def jam(self, case):
		case = case.split()
		C = int(case[0])
		combs = case[1:1+C]
		D = int(case[1 + C])
		opps = case[C+2:C+2+D]
		N = case[C+2+D]
		invoke = case[C+D+3]
		
		combs = dict(
			(''.join(sorted((a,b))),c) for a,b,c in combs
		)
		opps = map(''.join, map(sorted, opps))
		
		stack = []
		for e in invoke:
			stack.append(e)
			top = ''.join(sorted(stack[-2:]))

			if top in combs:
				stack.pop()
				stack.pop()
				stack.append(combs[top])
			elif any(
					''.join(sorted((e,x))) in opps
					for x in stack[:-1]
				):
				stack = []
				
		
		return "[%s]" % (", ".join(stack),)

if __name__ == "__main__":
	QualB.start()
