import sys
def check(str1,str2):
	ind1 = 0
	ind2 = 0
	temp = set([])
	while (ind2 < len(str2)):
		if (ind1==len(str1)):
			return 0
		else:
			if (str2[ind2] == "("):
				temp = set([])
				ind2 = ind2 + 1
				while (str2[ind2] != ")"):
					temp.add(str2[ind2])
					ind2 = ind2 + 1
					if (ind2 == len(str2)):
						return 0
				if (str1[ind1] not in temp):
					return 0
				
			else:
				if (str1[ind1] != str2[ind2]):
					return 0
			ind1 = ind1 +1
			ind2 = ind2 +1
	return 1
def checking(myset, pat):
	ret = 0
	for t in myset:
		if (check(t,pat)):
			ret = ret +1
	return ret
stringset = set([])
a = open("my.in")
p = a.readline()
t = p.split()
x = []
for u in t:
	x.append(int(u))
for k in xrange(x[1]):
	stringset.add(a.readline())
for k in xrange(x[2]):
	print "Case #"+str(k+1)+":",checking(stringset,a.readline())

