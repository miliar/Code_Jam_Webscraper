import string
import re

s = raw_input()
a = s.split()
l = int(a[0])
d = int(a[1])
n = int(a[2])
list = []

for i in range(d):
        s = raw_input()
        list.append(s)

for i in range(n):
        count = 0
        s = raw_input()
        s=string.replace(s, "(", "[")
        s=string.replace(s, ")", "]")
        for j in range(d) :
                if(re.match(s,list[j])):
                        count += 1
        print "Case #{0}:".format(1+i), count