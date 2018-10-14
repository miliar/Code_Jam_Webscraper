import sys, string#, re

class MyTree:
	def __init__(self):
		self.root = {}

	def add(self, word):
		root = self.root
		cur = root
		ind = 0
		if not word[ind] in root:
			root[word[ind]] = {}
			cur = root[word[ind]]
			ind += 1
		# while len(cur) != 0:
		while root and ind < len(word):
			if not word[ind] in cur:
				cur[word[ind]] = {}
			root = cur
			cur = cur[word[ind]]
			ind += 1
	
	def display(self):
		print self.root
			
	def get(self, str_):
		tmp = self.root
		for c in str_:
			tmp = tmp[c]
		return tmp

#m = re.compile("^\([^)]*\)")
def consume(word):
	l = []
	w = word 
	if w[0] == '(': 
		c = 1
		while w[c] != ')':
			l.append(w[c])
			c += 1
		w = w[c+1:len(w)]
	else:
		l.append(w[0])
		w = w[1:len(w)]
	return (w, l)
		
input_f = open(sys.argv[1],'r')
first_line = input_f.readline()
fline = first_line.split(' ')
words_length = string.atoi(fline[0])
dict_size = string.atoi(fline[1])
nb_cases = string.atoi(fline[2])
# print words_length
# print dict_size
# print nb_cases
## dict = {}
tree = MyTree()
for i in range(0, dict_size):
	word = input_f.readline().strip("\n")
	tree.add(word)
	## dict[word] = 1
## print dict
# tree.display()
for i in range(0, nb_cases):
	keys_list = []
	test = input_f.readline().strip("\n")
	(test, list) = consume(test)
	for item in list:
		if item in tree.root:
			keys_list.append(item)
	while test:
		(test, list) = consume(test)
		new_keys_list = []
		for j in range(len(keys_list)):
			for item in list:
				if item in tree.get(keys_list[j]):
					new_keys_list.append(keys_list[j]+item)
		keys_list = new_keys_list
	print "Case #" + str(i+1) + ": " + str(len(keys_list))
