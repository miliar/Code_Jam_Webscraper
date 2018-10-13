#!/usr/bin/env python3

mappings = {'q': 'z', 'y': 'a', 'e': 'o', 'z': 'q'}

example_input = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

example_output = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

for i in range(len(example_input)):
	if example_input[i] in (' ', '\n'):
		continue
	mappings[example_input[i]] = example_output[i]

for i in range(int(input())):
	inp = input().strip()
	out = ''.join([mappings[c] if c in mappings else c for c in inp])
	print('Case #%d: %s' % (i+1, out))
