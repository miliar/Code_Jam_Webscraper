from itertools import islice,chain

def contains_nums(s) :
	return any(ch.isdigit() for ch in s)

def parse_lines(lines) :
	return map(lambda s : s.strip(), islice(lines, 2, None))

case = 1
def format_solution(solution) :
	global case ; ans = f'Case #{case}: {solution}' ; case += 1
	return ans


def solve(block) :
	rows = len(block) ; cols = len(block[0])
	past_letters = set()
	for r in range(rows) :
		for c in range(1, cols) :
			if block[r][c-1] != '?' and block[r][c] == '?' :
				block[r][c] = block[r][c-1] # shift forwards
		for c in reversed(range(1, cols)) :
			if block[r][c-1] == '?' :
				block[r][c-1] = block[r][c] # shift backwards
	for r in range(1, rows) :
		for c in range(cols) :
			if block[r][c] == '?' :
				block[r][c] = block[r-1][c]
	for r in reversed(range(1, rows)) :
		for c in range(cols) :
			if block[r-1][c] == '?' :
				block[r-1][c] = block[r][c]
			
	return '\n' + '\n'.join(''.join(row) for row in block)

solf = open('solved_large.txt', 'w')
with open('A-large.in') as lines :
	block = []
	for line in parse_lines(lines) :
		if not contains_nums(line) :
			block += [list(line)]	
			continue
		print(format_solution(solve(block)), file = solf)
		block = []
	print(format_solution(solve(block)), file = solf)