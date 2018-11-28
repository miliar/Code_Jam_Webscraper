# count the last tidy number 
ncase = int(input())

def shrink(mylist):
	global doshrink
	lenOflist = len(mylist)
	for i in range(1,lenOflist):
		if mylist[i-1] > mylist[i]:
			mylist[i-1] = ( mylist[i-1] + 10 -1 ) % 10
			#print(mylist)
			ans = mylist[0:i] + [ 9 for x in mylist[i:]]
			#print(ans)
			doshrink = True
			return(ans)
	ans = mylist
	doshrink = False 
	return ans

for i in range(ncase):
	doshrink = True
	numbers = list(input())
	nms = [int(x) for x in numbers]
	while doshrink == True:
		nms = shrink(nms)
	print("Case #%d: %d" %(i+1, int(''.join([str(x) for x in nms]))))

