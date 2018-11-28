#!/usr/bin/python

f = open("./case_a.txt", 'r')
w = open("./out_a.txt", 'w')
test_num = int(f.readline())
i = 0
while i<test_num:
	pancake, flip = f.readline().split(' ')
	pancake = list(pancake)
	flip = int(flip)
	res = 0
	for a in range(0,len(pancake)-flip+1):
		if pancake[a] == '-':
			for b in range(a,a+flip):
				if pancake[b] == '-':
					pancake[b] = '+'
				else:
					pancake[b] = '-'
			res = res + 1
	i = i+1
	if '-' in pancake:
		res = 'Case #'+str(i)+': IMPOSSIBLE\n'
		w.write(res)
	else:
		res = 'Case #'+str(i)+': '+str(res)+'\n'
		w.write(res)
w.close()
f.close()
