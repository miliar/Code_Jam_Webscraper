s = " abcdefghijklmnopqrstuvwxyz"
s1= " yhesocvxduiglbkrztnwjpfmaq"

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
    for x in range(0,i.__len__()):
    	k = s.index(i[x])
    	res = res + s1[k]
    print res
