def main():
	t = int(input())
	tab_col = {
		"R": "YBG",
		"O": "B",
		"Y": "RBV",
		"G": "R",
		"B": "YRO",
		"V": "Y",
		}

	
	for t_i in range(t):
		n, r, o, y, g, b, v = map(int, input().split())
		d_i = {"R":r, "O":o, "Y": y, "G": g, "B": b, "V": v}
	
		table = [-1]*n
		impossible = False
	
		current = nextF("RYB", d_i)
		table[0] = current
		first = current
		d_i[current] -= 0.5
	
		index = 1
		while index < n:
			next = nextF(tab_col[current], d_i)
		
			if next == "":
				impossible = True
				break
			table[index] = next
			d_i[next] -= 1
			current = next
			index += 1
	
		if not impossible:
			if table[-1] not in tab_col[table[0]]:
				impossible = True
	
		if impossible:
			print("Case #%d: IMPOSSIBLE" % (t_i+1))
		else:
			print("Case #%d: %s" % (t_i+1, ''.join(table)))


def nextF(possibles, d_i):
	p_max = 0.7
	next = ""
	for second in "OGV":
		if second in possibles:
			if d_i[second] > p_max:
				p_max = d_i[second]
				next = second
	if next == "":
		for prem in "RYB":
			if prem in possibles:
				if d_i[prem] > p_max:
					p_max = d_i[prem]
					next = prem
	return next
main()