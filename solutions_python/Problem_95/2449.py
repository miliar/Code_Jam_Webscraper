et = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z'

dt = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q'

count = 0
for i in et:
	count = count +1

tmp = {}
for i in range(count):
	tmp[et[i]] = dt[i]

n =  int(raw_input())

for i in range(n):
	str = raw_input()
	ans = ''
	for s in str:
		ans+=tmp[s]
	print 'Case #%d:'%(i+1),ans

