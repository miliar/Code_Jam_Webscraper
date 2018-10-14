
def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

	
file_in = 'A-large.in'
file_out = 'out.txt'
with open(file_in,'rb') as fin, open(file_out,'w') as fout:
	lines = fin.read().splitlines()
	case = 1
	for l in lines[1:]:
		# print (l)
		_string = list(str(l.split()[:1]))
		k = int(l.split()[1])
		count =0
		i, j = 0, len(_string)
		while i<j:
			i = "".join(_string).find('-')
			if i == -1 or i+k >len(_string):
				break
			for x in range(i,i+k):
				if _string[x] == '-':
					_string[x] = '+'
				else:
					_string[x] = '-'
			count = count + 1
			# print (_string)

			j = "".join(_string).rfind('-')
			if j == -1 or (j-k+1 < 0):
				break
			if j-i < k:
				break
			for x in range(j-k+1,j+1):
				if _string[x] == '-':
					_string[x] = '+'
				else:
					_string[x] = '-'
			count = count+1
			# print (_string)

		if "".join(_string).find('-') > -1:
			answer = "IMPOSSIBLE"
		else:
			answer = str(count)
		output = 'Case #%d: %s\n' % (case,answer)
		fout.write(output)
		case += 1


		