
from decimal import *

t = int(raw_input())

for case in xrange(0,t):
	farmCost, farmRate, goal = [ Decimal(a) for a in raw_input().split(' ') ]
	farms = Decimal(0)
	farmTime = Decimal(0)
	time = goal / (farms * farmRate + 2) + farmTime
	farms = farms + 1
	farmTime = farmTime + (farmCost / (2 + (farms-1) * farmRate))
	newTime = goal / (farms * farmRate + 2) + farmTime
	while (newTime < time):
		time = newTime
		farms = farms + 1
		farmTime = farmTime + (farmCost / (2 + (farms-1) * farmRate))
		newTime = goal / (farms * farmRate + 2) + farmTime
	print( 'Case #{0}: {1}'.format(case+1,time) )
