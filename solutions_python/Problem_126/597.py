vowels = ['a', 'e', 'i', 'o', 'u']

def determin(name, l, result):

	if len(name) < l:
		return result

	for i in range(len(name) - l + 1):
		# i is first character in consecutive consonants
		for j in range(l):
			if (name[i + j] in vowels):
				# name[i + j] is vowel
				break
			if j == l - 1:
				#result = result + i + (len(name) - (i + l)) + 1
				result = result + (i + 1) * (len(name) - (i + l) + 1)
				#print 'name', name, 'result', result, 'name[i + 1:]', name[i + 1:]
				return determin(name[i + 1:], l , result)
	if i == len(name) - l:
		# name don't have consecutive consonants
		#print name
		return result

#f = open('sample.txt', 'r')
f = open ('A-small-attempt0.in', 'r')
f2 = open('outputA.txt', 'a')

input_number = 1
first_flg = 1

for line in f:
	line = line.split()
	if first_flg:
		num_of_input = int(line[0])
		first_flg = 0
	else:
		name = line[0]   
		l = int(line[1])

		result = 0
		result = determin(name, l, result)

		#print 'result', result

		f2.write('Case #' + str(input_number) + ': ' + str(result) + '\n')
		input_number = input_number + 1

f2.close()
f.close()