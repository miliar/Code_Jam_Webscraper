inp = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
       "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
       "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

out = ["our language is impossible to understand",
       "there are twenty six factorial possibilities",
       "so it is okay if you want to just give up"]

d = {}

def translate(str, d):
	result = ""
	for i in range(len(str)):
		if (str[i] in d.keys()):
			result += d[str[i]]
		else:
			result += str[i]
	return result
	
def make_dictionary():
	global d,inp,out
	for t in range(len(inp)):
		for i in range(len(inp[t])):
			if (inp[t][i] != ' '):
				d[inp[t][i]] = out[t][i]	
	d['q'] = 'z'
	d['z'] = 'q'
	
if __name__ == "__main__":
	make_dictionary()
	f = open('A-small-attempt3.in','r')
	fo = open('A.out','w');
	n = 0
	line = f.readline()
	line = f.readline()
	while (line != ''):
		n += 1
		fo.write('Case #{0}: {1}\n'.format(n,translate(line[:-1],d)))
		line = f.readline()
	f.close()
	fo.close()
	
#print d
