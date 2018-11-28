f = open('input.txt')


inpu = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']
samples = int(f.readline().strip())
demos = ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']
diction = {}
for k in range(3):
	
	#string = f.readline().strip()
	for char in range(len(inpu[k])):
		diction[inpu[k][char]] = demos[k][char]

diction['q'] = 'z'
diction['z'] = 'q'
print len(diction)
output = ''
for k in range(samples):
	
	string = f.readline().strip()
	newSt = ''
	for char in string:
		try:
			newSt += diction[char]
		except:
			newSt += char
	output += 'Case #' + str(k+1)+': ' + newSt + '\n'


o = open('output.txt', 'w')
o.write(output)
o.close

#print diction
#has = []

#for i in diction:
#	has.append(diction[i])
#has.sort()
#needs q
#print has
