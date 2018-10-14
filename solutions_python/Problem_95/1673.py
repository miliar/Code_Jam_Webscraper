import string

dict = {
	'y' : 'a',
	'e' : 'o',
	'q' : 'z'
}

seeds = (("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
		("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
		("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"))

for target, origin in seeds:
	for i in range(len(origin)):
		dict[target[i]] = origin[i]


for letter in string.ascii_lowercase:
	if letter not in dict.keys():
		key = letter
		break

for letter in string.ascii_lowercase:
	if letter not in dict.values():
		value = letter
		break

dict[key] = value

trans_table = string.maketrans("".join(dict.keys()), "".join(dict.values()))

fin = open("a-input.txt", "rb")
count = int(fin.readline())
fout = open("a-out.txt", "wb")

for i in range(1, count + 1):
	line = fin.readline()
	fout.write(("Case #%d: " % i) + string.translate(line, trans_table))

fin.close()
fout.close()



