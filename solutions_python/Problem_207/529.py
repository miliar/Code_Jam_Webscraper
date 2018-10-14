t = int(input())

def p(res):
	print("Case #" + str(i+1) + ": " + res)

def share_color(c1, c2):
	if c1 == c2: return True
	if c1 == 'R':
		return c2 == 'O' or c2 == 'V'
	if c1 == 'Y':
		return c2 == 'O' or c2 == 'G'
	if c1 == 'B':
		return c2 == 'G' or c2 == 'V'
	if c1 == 'G':
		return c2 != 'R'
	if c1 == 'O':
		return c2 != 'B'
	if c1 == 'V':
		return c2 != 'Y'

def validate_r(r):
	if share_color(r[0], r[-1]): return False
	for i in range(len(r)-1):
		if share_color(r[i], r[i+1]):
			return False
	return True

def switch_with_last(r, k):
	tr = list(r)

	tp = tr[k]
	tr[k] = tr[-1]
	tr[-1] = tp

	if validate_r(tr):
		r = ''.join(tr)

	return r



for i in range(t):


	N, R, O, Y, G, B, V = [int(i) for i in input().split()]
	r = ""

	last = ''
	first = ''

	if O > 0:
		if B < O:
			p("IMPOSSIBLE")
			continue
		if B == O:
			if Y > 0 or R > 0 or G > 0 or V > 0:
				p("IMPOSSIBLE")
				continue
			else:
				p('BO'*O)
				continue
		B -= (O+1)
		r += 'BO'*O+'B'
		first = 'B'
		last = 'B'
	if G > 0:
		if R < G:
			p("IMPOSSIBLE")
			continue
		if R == G:
			if Y > 0 or O > 0 or B > 0 or V > 0:
				p("IMPOSSIBLE")
				continue
			else:
				p('RG'*G)
				continue
		R -= (G+1)
		if r == '': first = 'R'
		r += 'RG'*G+'R'
		last = 'R'
	if V > 0:
		if Y < V:
			p("IMPOSSIBLE")
			continue		
		if Y == V:
			if R > 0 or O > 0 or B > 0 or G > 0:
				p("IMPOSSIBLE")
				continue
			else:
				p('YV'*V)
				continue
		Y -= (V+1)
		if r == '': first = 'Y'
		r += 'YV'*V+'Y'
		last = 'Y'

	echec = False


	while R > 0 or Y > 0 or B > 0:

		if R > 0 and ((R >= Y and R >= B and last != 'R') or (R >= Y and last=='B') or (R >= B and last=='Y')):
			if r == '': first = 'R'
			r += 'R'
			last = 'R'
			R -= 1
			continue
		if Y > 0 and ((Y >= R and Y >= B and last != 'Y') or (Y >= R and last=='B') or (Y >= B and last=='R')):
			if r == '': first = 'Y'
			r += 'Y'
			last = 'Y'
			Y -= 1
			continue
		if B > 0 and ((B >= Y and B >= R and last != 'B') or (B >= Y and last=='R') or (B >= R and last=='Y')):
			if r == '': first = 'B'
			r += 'B'
			last = 'B'
			B -= 1
			continue
		p('IMPOSSIBLE')
		echec = True
		break

	if not echec:
		if share_color(last, first):
			for k in range(len(r)):
				new_string = switch_with_last(r, k)
				if new_string != r:
					p(new_string)
					break
			else:
				p('IMPOSSIBLE')
		else:
			p(r)