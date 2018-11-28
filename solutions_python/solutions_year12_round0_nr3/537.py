import shlex

def length(n):
	n = str(n)
	i = n.__len__()
	return i

def rev(n):
	ln = length(n)
	l = []
	for x in range(0,ln-1):
		a = n % 10
		b = a*(10**(ln-1))
		n = n/10
		n = b + n
		if (n in l):
			temp = 0
		else:
			l.append(n)
	return l

def count(l,n,v1,v2):
	count = 0
	for i in l:
		if((n < i) and (i <= v2) and (i >= v1)):
			count = count + 1
	return count

a = raw_input()
try:
    a = int(a)
except ValueError:
    print "error occured"

mylist = []
i = 0
while i < a:
	b = raw_input()
	mylist.append(b)
	i = i + 1

z = 0
for i in mylist:
    res = "Case #"
    z = z + 1
    l = str(z)
    res = res + l + ": "
    zz = 0
    val2 = shlex.split(i)
    v1 = val2[0]
    v2 = val2[1]
    try:
    	v1 = int(v1)
    	v2 = int(v2)
    except ValueError:
    	print "error occured"
    for values in range(v1,v2 + 1):
    	zz = zz + count(rev(values),values,v1,v2)
    res = res + str(zz)
    print res
