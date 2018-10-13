s = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvaozq"
t = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upyeqz"

# a = []
# for ch in s:
# 	a.append(ch)
# a.sort()
# print a

# b = []
# for ch in t:
# 	b.append(ch)
# b.sort()
# print b

T = input()

for tc in range(0,T):
	a = raw_input()
	b = ""
	
	for i in range(0,len(a)):
		for j in range(0,len(s)):
			if s[j] == a[i]:
				b += t[j]
				break
	
	print "Case #" + str(tc + 1) + ": " + b
