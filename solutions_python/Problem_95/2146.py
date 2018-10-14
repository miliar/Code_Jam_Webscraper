

inputStr  = 'zyeq ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
outputStr = 'qaoz our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

index = -1
map = {}
for a in inputStr:
	index += 1
	if map.has_key(a):
		assert map[a] == outputStr[index]
	else:
		map[a] = outputStr[index]

#a-z + ' '
assert len(map) == 27

#how many lines are we reading?
num = int(raw_input())


for i in range(0, num):
	print 'Case #'+str(i+1)+': '+''.join(map[l] if map.has_key(l) else l for l in raw_input())
	