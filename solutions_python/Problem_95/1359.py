key={}

key['y'] = 'a'
key['e'] = 'o'
key['q'] = 'z'
key['z'] = 'q'

s1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s3="de kr kd eoya kw aej tysr re ujdr lkgc jv"

o1="our language is impossible to understand"
o2="there are twenty six factorial possibilities"
o3="so it is okay if you want to just give up"

for i in range(len(s1)):
	key[s1[i]] = o1[i]

for i in range(len(s2)):
	key[s2[i]] = o2[i]

for i in range(len(s3)):
	key[s3[i]] = o3[i]

file = open('in','r')
lines = file.readlines()
file.close()

linesout = []
toout = ''
for i in range(1,len(lines)):
	for j in range(len(lines[i])-1):
		toout += key[lines[i][j]]
	linesout.append('Case #' + str(len(linesout) + 1) + ': ' + toout + '\n')
	toout = ''
	
file = open('out','w')
file.writelines(linesout)