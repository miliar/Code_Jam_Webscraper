string1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeqz"
string2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aozq"

arr1 = ['a']*26 
arr2 = [';']*26 
for i in xrange(26):
	arr1[i] = chr(i+ord('a'))

for i in xrange(len(string1)):
	if(string1[i]!=' '):
		arr2[ord(string1[i]) - ord('a')] = string2[i]
	

x = int(raw_input())
for i in xrange(x):
	string = raw_input()
	ret = ""
	for c in string:
		if(c==' '):
			ret+=' '
			continue
		ret+=arr2[ord(c)-ord('a')]
	print "Case #"+str(i+1) +": ",ret
	
			
	

