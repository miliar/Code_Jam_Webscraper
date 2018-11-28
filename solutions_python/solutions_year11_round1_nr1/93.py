def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def parse_param():
    return map(int, raw_input().split())

def solve(N, P_D, P_G):
    if P_G == 100:
	if P_D != 100:
	    return "Broken"
	else:
	    return "Possible"
    if P_G == 0:
	if P_D != 0:
	    return "Broken"
	else:
	    return "Possible"
    n_D = 100 / gcd(P_D, 100)
    if n_D <= N:
	return "Possible"
    else:
	return "Broken"

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
	print "Case #%d:" % i,
	N, P_D, P_G = parse_param()
	print solve(N, P_D, P_G)

main()

