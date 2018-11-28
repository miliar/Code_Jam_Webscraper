#!/usr/bin/python
import sys
arr=[]
first=True
for lines in sys.stdin:
	if first:
		T=int(lines)
		first=False
	else:
		arr.append(lines.split())

for i in range(T):
	list1=arr[i*10+int(arr[i*10][0])]
	list2=arr[i*10+5+int(arr[i*10+5][0])]
	cnt=0
	for elem in list1:
		if elem in list2:
			cnt=cnt+1
			elem1=int(elem)

	if cnt == 0:
		print "Case #%d: Volunteer cheated!" %(i+1)
	elif cnt == 1:
		print "Case #%d: %d" %(i+1,elem1)
	else: 
		print "Case #%d: Bad magician!" %(i+1)


