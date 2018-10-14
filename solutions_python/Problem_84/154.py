def is_valid(i,j,R,C,pic):
	if(j>=0 and j<C and i>=0 and i<R and pic[i][j]=='#'):
		return True
	return False
def fun(R,C):
	pic = []
	for i in range(R):
		pic.append( list(raw_input()))

	started = False
	for i in range(R):
		for j in range(C):
			if(pic[i][j]=='#'):
				pic[i][j]='/'
				if(is_valid(i,j+1,R,C,pic)):
					pic[i][j+1]='\\'	
				else:
					print "Impossible"
					return ""
				if(is_valid(i+1,j,R,C,pic)):
					pic[i+1][j]='\\'	
				else:
					print "Impossible"
					return ""
				if(is_valid(i+1,j+1,R,C,pic)):
					pic[i+1][j+1]='/'	
				else:
					print "Impossible"
					return ""
	for i in range(len(pic)):

		string = ""
		for j in range(len(pic[i])):
			string+=pic[i][j]
		print string

tests = int(raw_input())
t = 1
while(t<=tests):
	inp = [int(x) for x in raw_input().split()]
	print "Case #%s:"%(t)
	fun(inp[0],inp[1])
	t+=1
	


#sortowanie
#from operator import itemgetter
#sorted(arr,key=itemgetter(2))

#import operator
#s = sum(map(operator.mul,arr1,arr2))
#r = reduce(operator.xor,a)
	
