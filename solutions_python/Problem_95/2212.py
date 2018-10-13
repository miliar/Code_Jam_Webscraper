test_input1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
test_input2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
test_input3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

test_output1 = 'our language is impossible to understand'
test_output2 = 'there are twenty six factorial possibilities'
test_output3 = 'so it is okay if you want to just give up'

mapping = {}
for (x, y) in zip(test_input1, test_output1):
	mapping[x] = y

for (x, y) in zip(test_input2, test_output2):
	mapping[x] = y

for (x, y) in zip(test_input3, test_output3):
	mapping[x] = y

mapping['q'] = 'z'
mapping['z'] = 'q'

ntc = int(raw_input())
for i in xrange(0, ntc):
	sentence = list(raw_input())
	for j in xrange(0, len(sentence)):
		sentence[j] = mapping[sentence[j]]
	print 'Case #%d: %s'%(i+1, "".join(sentence))

