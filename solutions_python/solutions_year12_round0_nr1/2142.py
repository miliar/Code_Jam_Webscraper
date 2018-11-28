
mapping = dict(
	zip("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand") + 
	zip("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities") + 
	zip("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
)
mapping['z'] = 'q'
mapping['q'] = 'z'
import string
print set(string.lowercase) - set(mapping.values())
print set(string.lowercase) - set(mapping.keys())

with open('A-small-attempt1.in') as input:
	N = int(input.readline())
	with open('A-small-attempt1.out', 'w') as output:
		for i, line in enumerate(input.readlines()):
			output.write("Case #{i}: {decoded}\n".format(i=i+1, decoded=''.join([mapping[ch] for ch in line[:-1]])))