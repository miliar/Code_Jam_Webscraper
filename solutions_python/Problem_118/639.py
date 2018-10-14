### make preset text
# -*- coding:utf-8 -*-
def third(u):
	i = str(u)
	l = len(i)
	a = l-1
	r = 1
	while r > 0:
		if i[a] == "1":
			if a > 0 :
				i = i[:a] + "0" + i[a+1:]
				a=a-1
				continue
			else:
				return -1
		if i[a] == "0":
			i = i[:a] + "1" + i[a+1:]
		r=r-1
	return i

def de(st):
	i = 0
	l = len(st)/2
	while i<l:
		if st[i] != st[-1*(i+1)]: return 0
		i=i+1
	return 1


i = 25
j = 0
k = 0
data = []
while i<=25:
	k = "1"
	t = ""
	j = 1
	while j<i:
		k = k + "0"
		j=j+1

	while 1:
		a = 0
		l = ""
		while a<len(k):
			l=k[a]+l
			a=a+1
		lst =k+l
		if i!=25:
			lst0=k+"0"+l
			lst1=k+"1"+l
			lst2=k+"2"+l
#		print lst
#		print lst0
#		print lst1
#		print lst2

		c = 0
		a = 0
		while a<len(k):
			c=c+(int(k[a])*int(k[a]))
			a=a+1
		c=c*2
		if c<10:
			dd = int(lst)*int(lst)
			if de(str(dd)):
				print dd
			if i!=25:
				dd = int(lst0)*int(lst0)
				if de(str(dd)):
					print dd
				dd = int(lst1)*int(lst1)
				if de(str(dd)):
					print dd
				dd = int(lst2)*int(lst2)
				if de(str(dd)):
					print dd

		k=third(k)
		if k == -1: break
		c = 0
		a = 0
	
	k = "2"
	j = 1
	while j<i:
		k = k + "0"
		j=j+1
	
	a = 0
	l = ""
	while a<len(k):
		l=k[a]+l
		a=a+1
	ls2 = k+t+l
	if i!=25:
		ls20=k+"0"+l
		ls21=k+"1"+l
		ls22=k+"2"+l

#	print ls2
#	print ls20
#	print ls21
#	print ls22
	dd = int(ls2)*int(ls2)
	if de(str(dd)):
		print dd
	if i!=25:
		dd = int(ls20)*int(ls20)
		if de(str(dd)):
			print dd
	
		dd = int(ls21)*int(ls21)
		if de(str(dd)):
			print dd
			
		dd = int(ls22)*int(ls22)
		if de(str(dd)):
			print dd
	i=i+1

print "dataset done"


### sort file
# -*- coding:utf-8 -*-

f = open("f.txt","r")
data = []

while 1:
	line  = f.readline()
	if not line:break
	data.append(int(line))
print "read done"
data.sort()
f.close

f = open("f.txt.sort",'w')
i = 0;
while i<len(data):
	f.write(str(data[i])+'\n')
	i=i+1


f.close





### run
# -*- coding:utf-8 -*-
f = open("result.txt","r") #preset file
data = []
while 1:
	line = f.readline()
	if not line:break
	data.append(int(line))

f.close

f = open("test.in","r")
lines  = int(f.readline())
i = 1

while i<=lines:
	#Problem Start	
	l = f.readline()
	r = l.split()
	a = int(r[0])
	b = int(r[1])

	r = 0
	j = 0
	s = 0
	while j<len(data):
		if data[j]>=a:s=1
		if s:
			if data[j]<=b:
				r=r+1
			else:
				break

		j=j+1
	
	print "Case #%d: %d" % (i,r)
	
	#End
	i=i+1
f.close
