def base2(a):
	k = ""
	t = a
	while (t != 0):
		k = k + str((t%2))
		t = t//2
	if (k == ""):
		return "0"
	else:
		return k
def ext_base2(thestr, thenum):
	p = thestr
	for k in range (thenum - len(thestr)):
		p = p+"0"
	return p
def cliper_on(number, clip):
	for k in range(number):
		if (ext_base2(base2(clip),number)[k] == "0"):
			return False
	return True

myin = open("a.in")
myout = open("a.out","w")
inputnum = int(myin.readline().strip())
for k in range(1,inputnum+1):
	p = myin.readline().strip().split()
	num = int(p[0])
	cli = int(p[1])
	myout.write("Case #")
	myout.write(str(k))
	myout.write(": ")
	if (cliper_on(num,cli)):
		myout.write("ON\n")
	else:
		myout.write("OFF\n")