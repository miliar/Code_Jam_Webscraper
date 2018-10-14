input = ['a zoo', 'ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']

output = ['y qee', 'our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']

map = {}

for i in range(len(input)):
	I = input[i]
	O = output[i]
	
	list_i = list(I)
	list_o = list(O)

	for j in range(len(list_i)):
		map[list_i[j]] = list_o[j]


k = map.keys()
v = map.values()

for i in range(97, 123):
	if chr(i) not in k:
		for j in range(97, 123):
			if chr(j) not in v:
				map[chr(i)] = chr(j)
				break
		break

T = int(raw_input())

for i in range(T):
	G = raw_input()
	list_G = list(G)

	S = []
	
	for j in list_G:
		S.append(map[j])

	S = ''.join(S)
	print 'Case #' + str(i+1) + ': ' + S 
