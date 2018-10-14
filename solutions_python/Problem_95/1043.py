import string

def solve():

	rosetta = {	"ejp mysljylc kd kxveddknmc re jsicpdrysi" : 
				"our language is impossible to understand" , 			
				"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" : 
				"there are twenty six factorial possibilities" ,
				"de kr kd eoya kw aej tysr re ujdr lkgc jv" : 
				"so it is okay if you want to just give up"}

	ct = { 'y':'a', 'e':'o', 'q':'z', 'z':'q'}

	for s in rosetta.keys():
		for i in range(len(s)):
			ct[s[i]] = rosetta[s][i]

	fi = open('googlerese_in2','r')
	fo = open('googlerese_out.txt','w')
	T = int(fi.readline())
	for t in xrange(1,T+1):
		s = fi.readline().strip()
		res = ''.join([ct[c] for c in s])
		fo.write("Case #%d: %s\n"%(t,res))
	fi.close()
	fo.close()
