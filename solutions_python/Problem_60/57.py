def get_arrays(n,k,b,t,places,speeds):
	possibles = []
	count = 0
	for i in xrange(n):
		if (b-places[n-1-i]*1.0)/speeds[n-1-i] > t:
			count+=1
		else:
			possibles.append(count)
	return possibles

def get_res(n,k,b,t,places,speeds):
	if k==0:
		return 0
	possibles = get_arrays(n,k,b,t,places,speeds)
	if len(possibles) < k:
		return "IMPOSSIBLE"
	if len(possibles)==1:
		return possibles[0]
	return reduce(lambda x,y: x+y, possibles[:k])
	
				
	
if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	for i in range(1,num+1):
		(n,k,b,t) = map(int,f.readline().strip().split(" "))
		places = map(int,f.readline().strip().split(" "))
		speeds = map(int,f.readline().strip().split(" "))
		print "Case #%d: %s" %(i,get_res(n,k,b,t,places,speeds))
		