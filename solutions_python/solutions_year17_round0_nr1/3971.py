import re

ipfile = open("A-small-attempt0.in",'rb')
lines = ipfile.readlines()
opfile = open("op.txt",'wb')

counter = 0
testcases = lines[0]

def flip(str):
	str = list(str)
	# print str
	for i in range(len(str)):
		if str[i] == '+':
			str[i]='-'
		elif str[i] == '-':
			str[i]='+'
	str = "".join(str)
	# print str
	return str

def possible(pstring,k,z,i):
	global counter
	if(len(pstring[z.start():])<k):
		opfile.write("Case #"+str(i)+": IMPOSSIBLE\n")
		return
	pstring = flip(pstring[z.start():z.start()+k])+pstring[z.start()+k:]
	counter+=1
	# print pstring
	z = re.search("-",pstring)
	if z:
		possible(pstring,k,z,i)
	else:
		opfile.write("Case #"+str(i)+": "+str(counter)+"\n")
		return

for i in range(1,len(lines)):
	counter = 0
	pstring = lines[i].split(" ")[0]
	k = int(lines[i].split(" ")[1])
	z = re.search("-",pstring)
	if z:
		# print z.start()
		possible(pstring,k,z,i)
	else:
		opfile.write("Case #"+str(i)+": 0\n")
