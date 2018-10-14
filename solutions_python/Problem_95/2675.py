s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2 = "our language is impossible to understand"
s3 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s4 = "there are twenty six factorial possibilities"
s5 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
s6 = "so it is okay if you want to just give up"
diz = {}

def MakeDict(a,b):
	global diz
	for i in xrange(1, len(a)):
		diz[a[i]] = b[i]
		
def ReadInput():
	l = []
	f = open("A-small-attempt2.in", "r")
	for line in f.readlines():
		l.append(line)
	for i in l: l[l.index(i)] = i[:-1]
	l.pop(0)
	Translate(l)
	

def Translate(l):
	fi = open("A-small-attempt2.out", "w")
	num = 1
	for phrase in l:
		f = ""
		for i in phrase:
			f = f + diz[i]
		a = "Case #"+str(num)+": "+f+"\n"
		fi.write(a)
		#print "Case #"+str(num)+": "+f
		num += 1
	fi.close()
# --- MAIN --- #

MakeDict(s1,s2)
MakeDict(s3,s4)
MakeDict(s5,s6)
print diz
diz['z'] = "q"
diz["q"] = "z"
ReadInput()
