import sys

encript = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','zq', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv' ] 
normal =  ['our language is impossible to understand','qz', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up' ]
dic = {}
def build_dic(in_put, out_put):
	for i in range(0, len(in_put)):
		for j in range(0, len(in_put[i])):
			dic[in_put[i][j]] = out_put[i][j]
		
		
f = open(sys.argv[1], 'r')
in_put = f.readlines()[1:]
build_dic(encript, normal)
for i in range(0, len(in_put)):
	output = ""
	in_put[i] = in_put[i].strip()
	for char in in_put[i]:
		output += dic[char]
	print "Case #" + str(i + 1) + ": " + output

	
