googlerese_testcase =  u"ejp mysljylc kd kxveddknmc re jsicpdrysi \
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
de kr kd eoya kw aej tysr re ujdr lkgc jv"

english_testcase = u"our language is impossible to understand \
there are twenty six factorial possibilities \
so it is okay if you want to just give up"

from UserString import MutableString

index = -1
# some translations from task example
translate_dict = {'a': 'y', 'o': 'e', 'z': 'q', 'q': 'z'}
for char in googlerese_testcase:
	index += 1
	translate_dict[char] = english_testcase[index]

test_count = int(raw_input())
test_cases = []

for test_index in xrange(test_count):
	test_cases.append(raw_input())

for test_index in xrange(test_count):
	result_string = MutableString()
	for char in test_cases[test_index]:
		result_string += translate_dict[char]
	print "Case #%d: %s" % (test_index + 1, result_string)

