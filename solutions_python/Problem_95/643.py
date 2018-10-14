import string

# create character mapping from Googlerese to English
sample_input = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv''' + "yeqz"
sample_input = [letter for letter in sample_input if letter in string.ascii_lowercase]
sample_output = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up''' + "aozq"
sample_output = [letter for letter in sample_output if letter in string.ascii_lowercase]
translator = dict(zip(sample_input, sample_output))
del(sample_input)
del(sample_output)

def translate_char(c):
	if c in translator:
		return translator[c]
	else:
		return c

def translate(text):
	return ''.join([translate_char(c) for c in text])

T = int(raw_input())

for case in xrange(1, T + 1):
	line = raw_input()
	print "Case #%d: %s" % (case, translate(line))

