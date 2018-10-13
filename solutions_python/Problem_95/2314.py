a = list('ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv')
b = list('our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up')
master = []
master1 = []

for i in range(1,len(a)):
	c = (a[i],b[i])
	d = (b[i],a[i])
	if c not in master: master.append(c)
	if d not in master1: master1.append(c)

master.append(('q','z'))
master.append(('z','q'))

dict = dict(master)

def convert(a):
	global dict
	blank = ""
	for i in list(a):
		try: blank += dict[i]
		except KeyError: blank += i
	return blank

fin = open("A-small-attempt7.in.txt")
fout = open("outputGoogle.out",'w')
num = int(fin.readline())
counter = 1

while counter <= num:
	line = fin.readline()
	case = "Case #" + str(counter) + ": " + convert(line)
	fout.write(case)
	counter += 1