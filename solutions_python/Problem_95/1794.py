#decode.py
#Matt Lough - sifrawr@gmail.com

#"Text to decode" : "Decoded"
mappings = {'a':'', 'b': '', 'c': '', 'd' : '', 'e' : 'o', 'f' : '', \
			'g' : '','h' : '', 'i' : '', 'j' : '', 'k' : '', 'l' : '', \
			'm' : '', 'n' : '', 'o' : '', 'p' : '', 'q' : 'z', 'r' : '', \
			's' : '', 't' : '', 'u' : '', 'v' : '', 'w' : '', 'x' : '', \
			'y' : 'a', 'z' : 'q', ' ': ' '}
			
def set_mappings():
	samples = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', \
			   'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', \
			   'de kr kd eoya kw aej tysr re ujdr lkgc jv']
	answers = ['our language is impossible to understand', \
			   'there are twenty six factorial possibilities', \
			   'so it is okay if you want to just give up']
			   
	for sampleNo in range(len(samples)):
		for i in range(len(samples[sampleNo])):
			mappings[samples[sampleNo][i]] = answers[sampleNo][i]
			
def decode(S):
	out = ''
	for x in S:
		out += mappings[x]
	return out
	
set_mappings()
n = int(raw_input())
for i in range(n):
	case = raw_input()
	print "Case #%i: %s" % (i + 1, decode(case))