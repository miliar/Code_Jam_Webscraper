def solve(unicorns):
	[n, r, o, y, g, b, v] = unicorns
	for unicorn in unicorns[1:]:
		if unicorn > n / 2:
			return 'IMPOSSIBLE'
	result = ''
	first_color = None
	while r > 0 or y > 0 or b > 0:
		sorted_colors = sorted([(r, 'R'), (y, 'Y'), (b, 'B')])
		next_color = sorted_colors[2][1]
		if len(result) == 0:
			first_color = next_color
		elif result[-1] == sorted_colors[2][1]:
			next_color = sorted_colors[1][1]
		if len(result) != n-1 and next_color != first_color and not has_other_colors(r, y, b, first_color):
			next_color = first_color

		result += next_color
		if next_color == 'R':
			r = r - 1
		elif next_color == 'Y':
			y = y - 1
		elif next_color == 'B':
			b = b - 1
	return result

def has_other_colors(r, y, b, color):
	if color == 'R':
		return y + b > 1
	if color == 'Y':
		return r + b > 1
	if color == 'B':
		return r + y > 1




def parse():
	unicorns = [int(i) for i in raw_input().split()]
	return unicorns

T = int(raw_input())
for t in range(1, T+1):
	print("Case #{0}: {1}".format(t, solve(parse())))
 
