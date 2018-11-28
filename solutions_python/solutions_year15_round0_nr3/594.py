# Problem C
import fileinput

rule = {
	'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k', '-1': '-1', '-i': '-i', '-j': '-j', '-k': '-k'},
	'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j', '-1': '-i', '-i': '1', '-j': '-k', '-k': 'j'},
	'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i', '-1': '-j', '-i': 'k', '-j': '1', '-k': '-i'},
	'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1', '-1': '-k', '-i': '-j', '-j': 'i', '-k': '1'},
	'-1': {'1': '-1', 'i': '-i', 'j': '-j', 'k': '-k', '-1': '1', '-i': 'i', '-j': 'j', '-k': 'k'},
	'-i': {'1': '-i', 'i': '1', 'j': '-k', 'k': 'j', '-1': 'i', '-i': '-1', '-j': 'k', '-k': '-j'},
	'-j': {'1': '-j', 'i': 'k', 'j': '1', 'k': '-i', '-1': 'j', '-i': '-k', '-j': '-1', '-k': 'i'},
	'-k': {'1': '-k', 'i': '-j', 'j': 'i', 'k': '1', '-1': 'k', '-i': 'j', '-j': '-i', '-k': '-1'}
}

def multiply(x, y):
	return rule[x][y]

def check_case(s):
	i = 0
	im = s[i]
	while i < len(s) - 2:
		if im == 'i':
			j = i + 1
			jm = s[j]
			while j < len(s) - 1:
				if jm == 'j':
					k = j + 1
					km = s[k]
					while k < len(s):
						k = k + 1
						if k < len(s):
							km = multiply(km, s[k])
					if km == 'k':
						return True
					else:
						return False
				j = j + 1
				if j < len(s) - 1:
					jm = multiply(jm, s[j])
			return False
		i = i + 1
		if i < len(s) - 2:
			im = multiply(im, s[i])
	return False

stdin = fileinput.input()
T = int(stdin.readline())
for ti in range(T):
	line = stdin.readline().strip().split(' ')
	L = int(line[0])
	X = int(line[1])
	s_pat = stdin.readline().strip()
	if s_pat == 'i' or s_pat == 'j' or s_pat == 'k':
		print('Case #' + str(ti + 1) + ': NO')
		continue
	s = X * s_pat
	if len(s) < 3:
		print('Case #' + str(ti + 1) + ': NO')
		continue
	if s == 'ijk':
		print('Case #' + str(ti + 1) + ': YES')
		continue

	if check_case(s) == True:
		print('Case #' + str(ti + 1) + ': YES')
	else:
		print('Case #' + str(ti + 1) + ': NO')

