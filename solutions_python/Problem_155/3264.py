with open('A-large.in') as f:
	words = [word.strip() for word in f]

output = open('output.txt','w')

t = int(words[0])

cases = []

for i in xrange(t+1):
	if (i > 0):
		temp = words[i]
		temp = temp.split(' ')
		case = list(temp)
		cases.append(case)

def count_friends(string):

	temp = {}
	length = len(string)

	for x in xrange(length):
		temp[x] = int(string[x])

	count = 0
	num = 0
	for x in xrange(length):
		if num < x:
			count += 1
			num += 1

		num += temp[x]
	
	return str(count)

for i in xrange(len(cases)):
	case_friend = count_friends(cases[i][1])
	text = 'Case #{}: '.format(i+1), case_friend, '\n'
	output.write(('').join(text))

output.close()