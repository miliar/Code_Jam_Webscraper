#!/usr/bin/python
import sys

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1



def proc(nums):
	[a,b,k]=nums.split(' ')

	olds=range(0,int(a))
	news=range(0,int(b))
	k=int(k)
	combos=[]
	ways=0
	for i in olds:
		for j in news:
			if (i & j) < k:
	#			print(str(i & j))
				ways+=1
#				combos.append([i,j])
#	print(str(combos))			
	return(str(ways))


while lines != [] and lines != ['']:
	output=proc(lines[0])

	print("Case #"+str(case)+": "+output)
	lines=lines[1:]
	case+=1
	
	
