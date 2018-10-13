from operator import xor
def Main():
	for case in range(int(raw_input())):
		N=int(raw_input())
		candies=sorted( [int(x) for x in raw_input().split()] )
		ans=[sum(candies)-candies[0],"NO"][reduce(xor,candies)!=0]
		print 'Case #{0}: {1}'.format(case+1,ans)

Main()
