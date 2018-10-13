sample="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
samp_ans = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
dict = {}
dict['q'] = 'z'
dict['z'] = 'q'
for i in range(len(sample)):
	dict[sample[i]] = samp_ans[i]
#print sorted(dict.values())
a = input()
for i in range(a):
	inp = raw_input()
	ans = "Case #"+str(i+1)+": "
	for j in inp:
		ans = ans+dict[j]
	print ans
