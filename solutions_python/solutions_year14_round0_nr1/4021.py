#! /usr/bin/env python
# By: Danesh Daroui

# returns tail of a list
def tail(l):
	return l[1:] if l else [];

# returns head of a list
def head(l):
	return l[0] if l else None;

# returns intersection between two lists
def inter(l1, l2):
	if (l1 and l2):
		if (head(l1) in l2): return [head(l1)]+inter(tail(l1), l2);
		else: return inter(tail(l1), l2);
	else: return [];

# open input and output files
fin=open('input.txt', 'r');
fout=open('output.txt', 'w');

# read number of test cases
nt=int(fin.readline());

for i in range(0, nt):
	# chosen row 1
	cr1=int(fin.readline());
	g1=[];
	for j in range(0, 4):
		g1.append(fin.readline());

	r1=[int(ii) for ii in g1[cr1-1].split(' ')];

	# chosen row 2
	cr2=int(fin.readline());
	g2=[];
	for j in range(0, 4):
		g2.append(fin.readline());

	r2=[int(ii) for ii in g2[cr2-1].split(' ')];


	res=inter(r1, r2);

	if (res==[]):
		ss="Case #"+str(i+1)+": Volunteer cheated!"
	elif (len(res)==1):
		ss="Case #"+str(i+1)+": "+str(res[0]);
	else:
		ss="Case #"+str(i+1)+": Bad magician!"
		
	# prepare the output string and then write it to the file
	print >> fout, ss 

# close input and output files
fin.close();
fout.close();

