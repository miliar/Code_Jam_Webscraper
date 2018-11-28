ENC_SAMPLE = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

DEC_SAMPLE = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

def build_dic(enc, dec):
	d = {"a":"y", "o":"e", "z":"q", "q":"z"}
	for x in zip(enc, dec):
		d[x[0]] = x[1]
	return d
	

def translate(text, dic):
	return "".join(dic[x] for x in text)
	
def main():
	T = int(raw_input())
	dic = build_dic(ENC_SAMPLE, DEC_SAMPLE)
	for i in range(T):
		text = raw_input()
		print "Case #%d: %s"%(i + 1, translate(text, dic))

main()	