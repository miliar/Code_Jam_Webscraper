#! /usr/bin/python

import sys

if len(sys.argv) < 3:
	exit(1)

finname = sys.argv[1]
foutname = sys.argv[2]

print "{} {}".format(finname,foutname)

fin=open(finname,"r")
fout=open(foutname,"w")

numcases=int(fin.readline());

print numcases

for case in range(0,numcases):
	fout.write ("Case #%d: " % (case+1))
	num=int(fin.readline());
	line=fin.readline();
	line=line.split();
	line2=list(line)
	print line
	print line2
	sum1=0;
	sum2=0;
	mdiff=0
	arlen=len(line)
	first=int(line.pop(0))
	for i in range(1,arlen):
		sec=int(line.pop(0))
		if first > sec:
			sum1+=first-sec
			if mdiff < first-sec:
				mdiff=first-sec
		first=sec
	first=int(line2.pop(0))
	for i in range(1,arlen):
		sec=int(line2.pop(0))
		if first > mdiff:
			sum2+=mdiff
		else:
			sum2+=first
		first=sec
	print "%d %d" % (sum1, sum2)
	fout.write("%d %d\n" % (sum1, sum2) )
			



