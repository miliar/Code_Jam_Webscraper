import pdb
import sys

def qmult(a, b):
	result = ''
	if '1' in a:
		result = list(b).pop()
	elif '1' in b:
		result = list(a).pop()
	elif 'i' in a:
		if 'i' in b:
			result = '-1'
		elif 'j' in b:
			result = 'k'
		elif 'k' in b:
			result = '-j'
	elif 'j' in a:
		if 'i' in b:
			result = '-k'
		elif 'j' in b:
			result = '-1'
		elif 'k' in b:
			result = 'i'
	elif 'k' in a:
		if 'i' in b:
			result = 'j'
		elif 'j' in b:
			result = '-i'
		elif 'k' in b:
			result = '-1'

	if ('-' in a and '-' not in b) or ('-' not in a and '-' in b):
		if '-' in result:
			return result[1]
		else: return '-' + result
	else:
		return result

def task(inFile):
	L, X = [int(n) for n in next(inFile).split(' ') if n != ' ' and n != '\n']
	string = next(inFile)
	string = string*X
	string = string.replace('\n', '')
	temp = '1'
	wanted = 'i'
	for x in range(0, len(string)):
		temp = qmult(temp, string[x])
		if temp == wanted:
			if wanted == 'i':
				wanted = 'j'
				temp = '1'
			elif wanted == 'j':
				wanted = 'k'
				temp = '1'
			elif wanted == 'k':
				if x == len(string) -1:
					return 'YES'


	return 'NO'


output = open('output.txt',  mode='w', encoding='utf-8')

with open(sys.argv[1], encoding='utf-8') as inFile:
	T = int(next(inFile))
	for t in range(0,T):
		output.write('Case #{0}: {1}\n'.format(t+1, task(inFile )))