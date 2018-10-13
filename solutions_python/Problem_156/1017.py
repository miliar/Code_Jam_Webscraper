inp = open('input_B_small.txt','r')
T = int(inp.readline().strip())
f = open('results_B_small.txt','w')

def rec(li,special):
	if max(li) < special:
		#print li, max(li),special
		return max(li) + special

	copy = [x for x in li]
	maxx = max(copy)
	copy.remove(maxx)
	minn = 10
	for k in range(1,maxx/2 + 1):
		#print k,maxx-k
		minn = min(minn, rec(copy + [k,maxx-k],special + 1))
	
	return min(minn,max(li)+special)


for t in range(0,T):
	d = int(inp.readline().strip())
	arr = eval("["+ inp.readline().strip().replace(" ",",")+"]")

	#print rec(arr,0)
	f.write('Case #'+str(t+1)+': '+str(rec(arr,0))+'\n')

inp.close()
f.close()
