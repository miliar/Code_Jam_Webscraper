#!/usr/bin/python
eng = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
goo = [' ', 'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
f = open("test.in")
count = 0
for line in f.readlines():
	line = line.strip()
	if count > 0:
		english = ""
		for char in line:
			i = goo.index(char)
			english = english + eng[i]
		print "Case #"+str(count)+": "+english
	count += 1
	
