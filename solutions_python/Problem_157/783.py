tests = int(raw_input())
mult_structure = {'1': {'1': '1', 'i': 'i', 'j' : 'j', 'k' : 'k'}, 
		  'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k' : '-j'}, 
		  'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'}, 
		  'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}}

for i in range(tests):
    result = None
    L , X = map(int, raw_input().split())
    input_string = str(raw_input())
    evaluation_string = ''
    for j in range(X):
	evaluation_string += input_string
    j = 0
    curr = '1'
    flagI = False
    flagJ = False

    while j < len(evaluation_string):
	if len(curr) == 2:
		curr = curr[1]
		curr = mult_structure[curr][evaluation_string[j]]
		if len(curr) == 2:
			curr = curr[1]
		else:
			curr = '-' + curr
	else:
		curr = mult_structure[curr][evaluation_string[j]]
	if curr == 'i' and not flagI:
		flagI = True
		curr = '1'
	if flagI and not flagJ and curr == 'j':
		flagJ = True
		curr = '1'
	j += 1
	#print curr,

    if flagI and flagJ and curr == 'k':
	result = 'YES'
    else:
	result = 'NO'
    print 'Case #'+ str(i+1)+': '+ str(result)
