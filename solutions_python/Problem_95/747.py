#original = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq"
#crypted  = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz"
#d = dict(zip(crypted, original))

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c',\
 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',\
 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p',\
 'y': 'a', 'x': 'm', 'z': 'q'}

try:
	nTests = int(raw_input())
	
	for test in xrange(1, nTests+1):
		line = raw_input()
		str = ''.join([d[c] for c in line])
		print "Case #%d: %s" % (test, str)

except EOFError:
	pass
