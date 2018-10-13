import shlex

a = raw_input()
try:
    a = int(a)
except ValueError:
    print "error occured"

def starapply(z,val3):
	if(z%3 == 0):
		if((z+3)/3 >= val3):
			return 1
	elif(z%3 == 1):
		if((z+2)/3 >= val3):
			return 1
	elif(z%3 == 2):
		if((z+4)/3 >= val3):
			return 1
	return 0
	
def starnapply(z,val3):
	if(z%3 == 0):
		if(z/3 >= val3):
			return 1
	if(z%3 == 1):
		if((z+2)/3 >= val3):
			return 1
	if(z%3 == 2):
		if((z+2)/3 >= val3):
			return 1
	return 0

mylist = []
i = 0
while i < a:
	b = raw_input()
	mylist.append(b)
	i = i + 1
	
z = 0
o = 0
for i in mylist:
	out = "Case #"
	o = o + 1
	valu = shlex.split(i)
	val1 = valu[0]
	val2 = valu[1]
	val3 = valu[2]
	try:
		val1 = int(val1)
		val2 = int(val2)
		val3 = int(val3)
	except ValueError:
		print "error occured"
	l1 = valu[3:]
	res = 0
	l1.sort()
	for j in l1:
		try:
			z = int(j)
		except:
			print "error occured"
		if(val2 != 0):
			if(starnapply(z,val3) == 1):
				res = res + 1
			elif((starapply(z,val3) == 1) and (z>=2)):
				res = res + 1
				val2 = val2 - 1
		elif(starnapply(z,val3) == 1):
			res = res + 1
	out = out + str(o) + ": " + str(res)
	print out
