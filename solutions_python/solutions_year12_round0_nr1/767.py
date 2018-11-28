import fileinput

sample = [("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
          ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
	  ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")]

# Build mapping for caeser cipher
dict = {}

dict['z'] = 'q'
dict['q'] = 'z'

for cipher, plain in sample:
	for c,p in zip(cipher,plain):
		assert ((c not in dict) or (dict[c]==p))
		dict[c]=p

def translate(cipher):
	return "".join(map(lambda c: dict[c], cipher))

count = 0
for line in fileinput.input():
	if not fileinput.isfirstline():
		count += 1
		print("Case #{}: {}".format(count,translate(line.strip())))
