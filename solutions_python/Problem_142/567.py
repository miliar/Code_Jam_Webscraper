import sys

input_file = 'A-small-attempt0.in'
output_file = 'A-small.out'

def run(resolve):
	oldstdin = sys.stdin
	fi = open(input_file, 'r')
	fo = open(output_file, 'w')
	sys.stdin = fi
	fo.write(process_cases(resolve))
	sys.stdin = oldstdin

def process_cases(resolve):
	case_total_num = int(input())
	result = ''
	for i in range(case_total_num):
		res = 'Case #%d: %s' % (i + 1, resolve(i+1))
		print(res)
		result = '%s%s\n' % (result, res)
	return result

def resolve(case_num):
	n = int(input())
	c = []
	t = None
	for i in range(n):
		s = input()
		tmp = ''
		last = ''
		for x in s:
			if x == last:
				continue
			last = x
			tmp += x
		if t is None:
			t = tmp
		elif t != tmp:
			return 'Fegla Won'
		c.append(s)
	total = 0
	for i in range(n):
		total += ed2(c[i], t, t)
	for i in range(n):
		tmp = 0
		for j in range(n):
			if i == j:
				continue
			tmp += ed2(c[i], c[j], t)
			#print(t,c[i], c[j], ed2(c[i], c[j], t), i)
		total = min(tmp, total)
	return total
	
def ed2(s1, s2, t):
	res1 = ed3(s1, t)
	res2 = ed3(s2, t)
	total = 0
	for i in range(len(t)):
		total += abs(res1[i] - res2[i])
	return total
	
def ed3(s, t):
	res = [0 for i in range(len(t))]
	if s == t:
		return res
	last = s[0]
	idx = 0
	for c in s[1:]:
		if c == last:
			res[idx] += 1
		else:
			last = c
			idx += 1
	return res
		
	
		
	
	
def ed(s1, s2):
	len1 = len(s1)
	len2 = len(s2)
	matrix = [[i+j for j in range(len2 + 1)] for i in range(len1 + 1)]
	for row in range(len1):
		for col in range(len2):
			comp = [matrix[row+1][col]+1, matrix[row][col+1]+1]
			if s1[row] == s2[col]:
				comp.append(matrix[row][col])
			else:
				comp.append(matrix[row][col]+1)
			if row > 0 and col > 0:
				if s1[row] == s2[col-1] and s1[row-1] == s2[col]:
					comp.append(matrix[row-1][col-1]+1)
			matrix[row+1][col+1] = min(comp)
	return matrix[len1][len2]

if __name__ == '__main__':
	run(resolve)
		