## Thang Bui

dumb = "yhesocvxduiglbkrztnwjpfmaq"

fin = open("input.txt", 'r')
fou = open("output.txt", 'w')
inlines = fin.readlines()

line0 = inlines[0]
nocases = int(line0)
print nocases
for i in range(nocases):
	str1 = 'Case #' + str(i+1) + ': '
	fou.write(str1)
	line = inlines[1+i]
	line = line[:-1].lower()
	for j in range(len(line)):
		c = line[j]
		print '\t', c
		if c == ' ':
			fou.write(c)
		else:
			n = ord(c) - 97
			d = dumb[n]
			fou.write(d)
	fou.write('\n')
	
fin.close()
fou.close()
