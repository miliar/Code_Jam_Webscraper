f = open('A-small.in', 'r')
lines = f.readlines()

a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

list_a = []
list_b = []

for i in range(0, len(a)):
	if not a[i] in list_a:
		list_a.append(a[i])
		list_b.append(b[i])

list_a.append('z')
list_b.append('q')

list_a.append('q')
list_b.append('z')

for i in range(1, len(lines)):
	line = lines[i]
	l_line = list(lines[i])
	for j in range(0, len(line)-1):
 		try:
			index = list_a.index(line[j])
			l_line[j] = list_b[index]
	        except ValueError:
			continue

	print "Case #" + str(i) + ": " + "".join(l_line),
