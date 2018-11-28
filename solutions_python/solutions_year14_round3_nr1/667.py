import sys
import math
import fractions

T = int(sys.stdin.readline())
def main():
	for case in range(1,T+1):
		res = solve(case)
		sys.stdout.write("Case #{}: {}\n".format(case, res));


def solve(case):
	pq = sys.stdin.readline().split("/")
	p = int(pq[0])
	q = int(pq[1])

	lcm = fractions.gcd(p,q)

	p = p/lcm
	q = q/lcm

	n = math.log(q)/math.log(2)

	if n.is_integer() == False:
	 	return "impossible"

	n = int(n)

	m = math.log(p)/math.log(2)

	m = int(m)

	gen = n-m;

	return gen;


main()
