inn = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
out = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
d = dict(zip(inn,out))
d['z'] = 'q'
d['q'] = 'z'
tests = input()
for i in range(1,tests+1):
	line = raw_input()
	line = map(lambda x: d[x], line)
	print "Case #"+str(i)+": "+"".join(line)
