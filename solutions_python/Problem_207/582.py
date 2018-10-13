def next_color(color, available, prefer=[]):
	max = 0
	next = None
	for c in available:
		if color[c] > max:
			max = color[c]
			next = c
		elif color[c] == max and max > 0 and c in prefer:
			next = c
	return next


def solve(N, R, O, Y, G, B, V):
	if O > B or G > R or V > Y:
		return "IMPOSSIBLE"

	color = {
		"R": R,
		"Y": Y,
		"B": B,
		"O": O,
		"G": G,
		"V": V
	}
	color2 = ["O", "V", "G"]
	color_map = {
		"B": "O",
		"Y": "V",
		"R": "G"
	}
	color_map2 = {
		"O": "B",
		"V": "Y",
		"G": "R"
	}
	result = ""
	while len(result) < N:
		l = len(result)
		if l == 0:
			n = next_color(color, color.keys(), prefer=[color2])
		else:
			prefer = [result[0]]
			if result[-1] in color2:
				available = [color_map2[result[-1]]]
			else:
				available = [c for c in color.keys()]
				available.remove(result[-1])
				prefer = [color_map[result[-1]]] + prefer
			n = next_color(color, available, prefer=prefer)

		if n is None:
			return "IMPOSSIBLE"
		result += n
		color[n] = color[n] - 1

	if len(result) > 1:
		if result[0] == result[-1]:
			return "IMPOSSIBLE"
		elif result[-1] in color2 and color_map[result[0]] != result[-1]:
			return "IMPOSSIBLE"
		elif result[0] in color2 and color_map2[result[0]] != result[-1]:
			return "IMPOSSIBLE"
	return result


t = int(raw_input())

for i in range(1, t + 1):
	N, R, O, Y, G, B, V = map(int, raw_input().strip().split())
	print("Case #%d: %s" % (i, solve(N, R, O, Y, G, B, V)))
