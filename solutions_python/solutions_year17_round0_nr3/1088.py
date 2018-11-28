import math
def calstat(mydict):
	#print("analysis")
	#print(mydict)
	newdict = {}
	for key in mydict:
		mtpl = mydict[key]
		if key %2 == 0 :
			tmpkey1 = key//2
			tmpkey2 = key//2 -1
			if tmpkey1 in newdict:
				newdict[tmpkey1] = newdict[tmpkey1] + 1 * mtpl
			else:
				newdict[tmpkey1] = mtpl
			
			if tmpkey2 in newdict:
				newdict[tmpkey2] = newdict[tmpkey2] + 1 * mtpl
			else:
				newdict[tmpkey2] = 1 * mtpl

		else:
			tmpkey = (key-1)//2
			if tmpkey in newdict:
				newdict[tmpkey] = newdict[tmpkey] + 2 * mtpl
			else:
				newdict[tmpkey] = 2 * mtpl
	#print(newdict)
	return(newdict)

ncase = int(input())
for i in range(ncase):
	info = input().split()
	nslots = int(info[0])
	usrs = int(info[1])
	level = int(math.log(usrs,2)) + 1 
	#print("level is", level)
	pos = usrs - ( 2 ** (level -1) -1 )
	#print("pos is", pos)
	mydict = {nslots:1}
	for j in range(level-1):
		mydict = calstat(mydict)
	thekey = max(mydict.keys())
	thevalue = mydict[thekey]
	if pos <= thevalue:
		ans = thekey
	else:
		ans = min(mydict.keys())
	#print(ans)
	print("Case #%d: %d %d" %(i+1, ans//2, (ans-1)//2))