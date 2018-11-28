import string, sys

# take input
filename = sys.argv[1]
f = open(filename,'r')

# variable declarations
lists = {}
excluded = []
g = ""

# generate alphabet dictionary
dicts = string.ascii_lowercase
for letter in dicts:
	lists[letter] = 'NULL'

# sample data to learn from
var1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jv"

var2 = "our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give up"

# convert vars to 'newline'-less strings
var1 = var1.split('\n')
str1 = ''.join(var1)
var2 = var2.split('\n')
str2 = ''.join(var2)

# learn from sample data and store mapping in lists
i = 0
lim = len(str1)
while i<lim:
	temp = str1[i]
	lists[temp] = str2[i]
	i = i+1

# find which letters aren't mapped in the sample
for x in dicts:
	i = 0
	contains = 0
	while i<lim:
		if x !=	str1[i] and x!=' ':
			contains = 1
		else:
			contains = 0
			i=lim
		i = i+1
	if contains == 1:
		excluded.append(x)
		
# mapping of remaining assumed
lists['q'] = 'z'
lists['z'] = 'q'

# remove '\n' in given file and read contents to a variable filecontents
filecontents = f.readlines()
for x in filecontents:
	x = x[0:-2]
filecontents = filecontents[1:]

# real processing
case_no = 1
for y in filecontents:
	i = 0
	tempstr = []
	while i<len(y):
		if y[i] == "\n":
			i = len(y)
		else:
			tempstr.append(lists[y[i]])
		i = i+1
	result = ''.join(tempstr)
	print "Case #" + str(case_no) + ": " + result
	case_no = case_no + 1
	
f.close()