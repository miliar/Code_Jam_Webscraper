str1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
str2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
li={}
for i in xrange(len(str1)):
	li[str1[i]]=str2[i]
li['z']='q'
li['q']='z'
t=int(raw_input())
for testCase in xrange(t):
	ans=""
	string=raw_input()
	for i in xrange(len(string)):
		#print string[i],
		ans+=li[string[i]]
	print "Case #"+str(testCase+1)+":",ans
