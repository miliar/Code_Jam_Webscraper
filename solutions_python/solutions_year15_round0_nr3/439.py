f = open('C-small-attempt0.in')
fw = open('C-small-attempt0.out', 'w')

mapping = {}
mapping['1'] = {'1':'1', 'i':'i', 'j':'j', 'k':'k', '-1':'-1', '-i':'-i', '-j':'-j', '-k':'-k'}
mapping['i'] = {'1':'i', 'i':'-1', 'j':'k', 'k':'-j', '-1':'-i', '-i':'1', '-j':'-k', '-k':'j'}
mapping['j'] = {'1':'j', 'i':'-k', 'j':'-1', 'k':'i', '-1':'-j', '-i':'k', '-j':'1', '-k':'-i'}
mapping['k'] = {'1':'k', 'i':'j', 'j':'-i', 'k':'-1', '-1':'-k', '-i':'-j', '-j':'i', '-k':'1'}
mapping['-1'] = {'1':'-1', 'i':'-i', 'j':'-j', 'k':'-k', '-1':'1', '-i':'i', '-j':'j', '-k':'k'}
mapping['-i'] = {'1':'-i', 'i':'1', 'j':'-k', 'k':'j', '-1':'i', '-i':'-1', '-j':'k', '-k':'-j'}
mapping['-j'] = {'1':'-j', 'i':'k', 'j':'1', 'k':'-i', '-1':'j', '-i':'-k', '-j':'-1', '-k':'i'}
mapping['-k'] = {'1':'-k', 'i':'-j', 'j':'i', 'k':'1', '-1':'k', '-i':'j', '-j':'-i', '-k':'-1'}

rev_mapping = {}
rev_mapping['1'] = {'i':'-i', 'j':'-j', 'k':'-k'}
rev_mapping['i'] = {'i':'1', 'j':'k', 'k':'-j'}
rev_mapping['j'] = {'i':'-k', 'j':'1', 'k':'i'}
rev_mapping['k'] = {'i':'j', 'j':'-i', 'k':'1'}
rev_mapping['-1'] = {'i':'i', 'j':'j', 'k':'k'}
rev_mapping['-i'] = {'i':'-1', 'j':'-k', 'k':'j'}
rev_mapping['-j'] = {'i':'k', 'j':'-1', 'k':'-i'}
rev_mapping['-k'] = {'i':'-j', 'j':'i', 'k':'-1'}

cases = int(f.readline())
for case in range(cases):
	print(case + 1)
	L, X = f.readline().split()
	L = int(L)
	X = int(X)
	input_str = f.readline()
	input_str = input_str[0:L] * X
	index = 0
	ans = 'NO'
	left_eval = '1'
	for c in input_str:
		left_eval = mapping[left_eval][c]
		if left_eval == 'i':
			j_and_k = input_str[index+1:]
			if len(j_and_k) < 2:
				break
			mid_eval = '1'
			right_eval = '1'
			for d in j_and_k:
				right_eval = mapping[right_eval][d]
			for p in range(len(j_and_k) - 1):
				mid_eval = mapping[mid_eval][j_and_k[p]]
				right_eval = rev_mapping[right_eval][j_and_k[p]]
				if mid_eval == 'j' and right_eval == 'k':
					ans = 'YES'
					break
			if ans == 'YES':
				break
		index += 1
	fw.write('Case #' + str(case + 1) + ': ' + ans + '\n')


fw.close()
f.close()
