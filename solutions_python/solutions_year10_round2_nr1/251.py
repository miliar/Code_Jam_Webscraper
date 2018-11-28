#!/usr/bin/python

string = raw_input()
numcase = int(string)

for i in range(numcase):
	
	string = raw_input()
	l = string.strip().split()
	N = int(l[0])
	M = int(l[1])
	
	existing = []
	for j in range(N):
		string = raw_input()
		existing.append(string.strip())
	
	new = []
	for k in range(M):
		string = raw_input()
		splitted = string.strip().split('/')
		directories = ""
		for i3 in range(len(splitted)-1):
			directories = directories + '/'+str(splitted[i3+1])
			new.append(directories)
	
	print "Case #%d: %d" %(i+1, len(set(new) - set(existing)))			
