english = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

googler = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

translate_char = {}

for (echar, gchar) in zip(english, googler):
	translate_char[gchar] = echar

translate_char['q'] = 'z'
translate_char['z'] = 'q'

with open('A-small-attempt2.in', 'r') as fin, open('A-small-attempt2.out', 'w') as fout:
	fin.readline()
	for i, line in enumerate(fin):
		fout.write('Case #' + str(i+1) + ': ')
		fout.write(''.join([translate_char.get(char, '') for char in line]))
