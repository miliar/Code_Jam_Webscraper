# -*- coding: utf-8 -*-
import re

f = open("A-large.in")
w = open("A-large.out","w")

(L, D, N) = map(int, f.readline().strip("\n").split(" "))

words = []
patterns = []

for i in range(D):
    words.append(f.readline().strip("\n"))
    
for i in range(N):
    patterns.append(f.readline().strip("\n").replace("(","[").replace(")","]"))
    
for i in range(N):
    count = 0
    pattern = patterns[i]
    y = re.compile(pattern)
    for word in words:
	z = re.match(y, word)
	if z:
	    count+=1   
    
    w.write("Case #%d: %d\n" % (i+1, count))

w.close()
    
