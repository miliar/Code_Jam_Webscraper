#!/usr/bin/python
import sys

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1
while lines != [] and lines != ['']:
	row1=lines[int(lines[0])].split(' ')
	row2=lines[5 + int(lines[5])].split(' ')
	matches=[]
	for i in row1:
		if i in row2:
			matches.append(i)

	output="Bad magician!"
	if len(matches) == 0:
		output='Volunteer cheated!'
	if len(matches) == 1:
		output=str(matches[0])
	
	print("Case #"+str(case)+": "+output)
	lines=lines[10:]
	case+=1
	
	
