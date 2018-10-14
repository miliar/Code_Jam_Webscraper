def isTidy(n):
    s = str(n)
    previous = int(s[0])
    for c in s:
        current = int(c)
        if current < previous:
            return False
        previous = current
    return True

def solve(n):
	s = str(n)
	sol = []
	previous = int(s[0])
	tidy = True
	for i, c in enumerate(s):
		current = int(c)
		if current < previous:
			tidy = False
			break
		sol.append(current)
		previous = current
	if not tidy:
		sol[-1] = sol[-1] - 1
		for _ in range(i, len(s)):
			sol.append(9)
	sol = int(''.join(map(str, sol)))
	if isTidy(sol):
		return sol
	else:
		return solve(sol)

sols = []

with open('B-large.in') as f:
	t = int(f.readline())
	for i in range(t):
		n = int(f.readline())
		sols.append(solve(n))

with open('sols-large-B.txt', 'w') as f:
	for i, y in enumerate(sols):
		f.write('Case #{}: {}\n'.format(i+1, y))