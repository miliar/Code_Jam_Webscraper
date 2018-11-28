def f(n, ch1, ch2):
	return (ch2 + ch1) * n + ch2

t_no = int(input())

for t in range(1, t_no + 1):
	#r, y, b
	n, r, o, y, g, b, v = [int(x) for x in input().split()]
	
	if o == b and o + b == n:
		ans = 'OB' * o
	elif g == r and g + r == n:
		ans = 'GR' * g
	elif v == y and v + y == n:
		ans = 'VY' * v
	else:		
		if (o == 0 or b > o) and (g == 0 or r > g) and (v == 0 or y > v):
			b -= o
			r -= g
			y -= v

			l = []
			l.append((r, 'R'))
			l.append((y, 'Y'))
			l.append((b, 'B'))
	
			l.sort()
			l.reverse()
	
			if l[1][0] + l[2][0] >= l[0][0]:
				ans = [l[0][1]] * l[0][0]
				for i in range(l[1][0]):
					ans[i] = ans[i] + l[1][1]
				for pos in range(l[1][0], l[1][0] + l[2][0]):
					i = pos % l[0][0]
					ans[i] = ans[i] + l[2][1]
				ans = ''.join(ans)
				for i in range(len(ans)):
					if ans[i] == 'R':
						ans = ans[:i] + f(g, 'G', 'R') + ans[i+1:]
						break
				for i in range(len(ans)):
					if ans[i] == 'B':
						ans = ans[:i] + f(o, 'O', 'B') + ans[i+1:]
						break
				for i in range(len(ans)):
					if ans[i] == 'Y':
						ans = ans[:i] + f(v, 'V', 'Y') + ans[i+1:]
						break
			else:
				ans = 'IMPOSSIBLE'
		else:
			ans = 'IMPOSSIBLE'

	print("Case #{}: {}".format(t, ans))
