#!/usr/bin/python

f=open("alien.txt");

line=f.readline();

values=line.split();

L=int(values[0]);
D=int(values[1]);
N=int(values[2]);

words=[]

for i in range(0,D):
	words.append(f.readline()[:L]);

index=0;
for i in range(0,N):
	index+=1;
	p=f.readline();
	patterns=[];
	group=0;
	for c in p[:-1]:
		if c=='(' and group:
			abort();
		elif c=='(':
			group=1;
			patterns.append([]);
		elif c==')':
			group=0;
		elif group:
			patterns[-1].append(c);
		else:
			patterns.append([c]);
	#print patterns

	#Ok, now check if words are into patterns
	count=0;
	for w in words:
		valid=1;
		for i in range(0,L):
			if not (w[i] in patterns[i]):
				valid=0;
				break;
		if valid:
			count+=1;
	print "Case #"+str(index)+": "+str(count)

