f = open("C-small-attempt3.in","r")
fo = open("op.txt","w")

class check_for_val:
	def __init__(self,val):
		self.last_res = -1
		self.a = -1
		self. b = -1
		self.val = val
		self.total = ''
	def push(self,char):

		self.total += char

		if char == self.val and self.last_res == -1 and self.a == -1 and self.b == -1 :
			return True

		print self.last_res,char,self.val

		if self.last_res == -1:
			
			if self.b == -1 and self.a != -1:
				self.b = char

			if self.a != -1 and self.b != -1:
				self.last_res = table(self.a,self.b)
				#print "first res:",self.last_res,self.a, self.b
			self.a = char

		else:
			a = self.last_res
			b = char

			self.last_res = table(a,b)
			new_string = ''

		if self.last_res == self.val:
			# print "*"*80
			# print self.total
			return True
		else:
			return False


def table(a,b):

	#print "-->",a,b
	if a == b:
		return '-1'

	invert = False

	if len(a) > 1:
		a = a.split('-')[1]
		invert = not invert
	if len(b) > 1:

		invert = not invert
		b = b.split('-')[1]

	res = '*'

	if a == '1' :
		res = b
	elif b == '1':
		res =a

	elif a == 'i' and b == 'j':
		res = 'k'
	elif a == 'j' and b == 'i':
		res = '-k'
	elif a == 'i' and b == 'k':
		res = '-j'
	elif a == 'k' and b == 'i':
		res = 'j'
	elif a == 'j' and b == 'k':
		res = 'i'
	elif a == 'k' and b == 'j':
		res = '-i'
	else:
		if a == b and invert == True:
			return '1'


	if invert:
		if len(res) > 1:
			res = res.split('-')[1]
		else:
			res = '-' + res

	return res


def same(line):

	first = line[0]

	for i in range(len(line)):
		if i != 0:
			if first != line[i]:
				return False
	return True

def gen_sub_strings(string):

	val_i =check_for_val('i')
	val_j =check_for_val('j')
	val_k =check_for_val('k')

	ln = len(string)

	substrings = []
	for i in range(ln-2):

		if val_i.push(string[i]):

			# print "i found"
			new_len = len(string[i+1:])
			new_string = string[i+1:]
			for j in range(new_len):
				# print "pushing",new_string[j]
				if val_j.push(new_string[j]):
					# print "j found"
					substrings.append([string[i:],new_string[:j],new_string[j+1:]])
					return substrings

	return substrings




def eval_string(string):
	
	while True:

		if len(string) == 2 and string.find('-') == 0:
			return string
		if len(string) == 1:
			return string
			
		a = ''
		b = ''

		new_string = ''


		if string[0] == '-':
			a = '-'+ string[1]
			if string[2] == '-':
				b = '-'+ string[3]
				new_string = string[4:]
			else:
				new_string = string[3:]
				b = string[2]
		else:
			a = string[0]
			if string[1] == '-':
				b = '-'+ string[2]
				new_string = string[3:]
			else:
				b = string[1]
				new_string = string[2:]

		res = table(a,b)

		#print res,new_string

		string = res + new_string
		#print string
		#s = raw_input()

def get_ans(line,multiple):

	if same(line):
		return "NO"

	if len(line) < 3 and multiple == 1:
		return "NO"

	sub_strings = gen_sub_strings(line*multiple)

	if len(sub_strings) == 0:
		return "NO"

	# print 30*'-'
	# for s in sub_strings:
	# 	print s

	# print 30*'-'
	for strings in sub_strings:
		if eval_string(strings[2]) == 'k':
			return "YES"

	return "NO"

def main():

	total_test_case = int(f.readline().split("\n")[0])

	for i in range(total_test_case):

		splitted = f.readline().split('\n')[0].split(' ')

		ln = int(splitted[0])
		multiple = int(splitted[1])

		line = f.readline().split('\n')[0]

		#print line,multiple
		ans = get_ans(line,multiple)
		print ans

		# print ln,multiple,line*multiple
		fo.write("Case #"+str(i+1)+": "+str(ans)+"\n")

main()
#print table('-i','-j')


# ss = gen_sub_strings('abcdefg')
# #	print ss
# for s in ss:
# 	print s

# fo.close()