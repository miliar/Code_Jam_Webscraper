input='''155 910
461 461
123 985
182 946
20 64
114 978
172 944
966 966
146 935
190 933
159 977
114 938
158 922
10 99
175 942
130 912
186 911
151 952
103 942
233 563
173 989
113 968
10 10
104 931
154 990
162 939
162 961
120 957
112 971
135 943
134 928
1 2
149 935
161 961
188 977
136 944
116 981
108 977
142 970
7 8
100 999
185 967
316 997
109 922
37 67
148 993
175 177
132 971
190 982
124 923'''.split("\n")

from collections import deque


import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


dict = {}

def recycled(a,b,c):
	s = str(c)
	d = deque(s)
	z = 0
	values = []
	for i in range(len(s)):
		d.rotate(1)
		i=""
		for x in d:
			i+=x
		i = int(i)
		if i>=a and i<=b:
			if i in dict:
				return 0
			dict[i] = 1
			values.append(i)
	if len(values)>=2:
		z += nCr(len(values),2)
	return z
for i, line in enumerate(input):
	a,b = line.split()
	a,b = int(a), int(b)
	z=0
	dict = {}
	for e in range(a,b):
		z+=recycled(a,b,e)
		if e%100000==0:
			print e
	print "Case #{0}: {1}".format(i+1,z)

