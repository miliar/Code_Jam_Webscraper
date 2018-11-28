#go brute force
#N can be 1 or 2 or 3

#is total possible with best
def possible(total, surp, best):
	if best == 0:
		return 1
	elif best == 1:
		if surp:
			#best>=1 and surp means total must be at least 2+0+0=2
			if total >=2:
				return 1
			else:
				return 0
		else:
			#best >=1 and not surp means total must be at least 1
			if total >=1:
				return 1
			else:
				return 0
	if not surp:
		#now the results are between (best-1, best-1, best) and 30
		if total >= (3*best-2):
			return 1
		else:
			return 0
	else:
		#now the results are between (best-2, best-2 ,best) and 30
		if total >= (3*best-4):
			return 1
		else:
			return 0

def case(numGooglers, numSurp, best, totals):
	if numGooglers==1:
		if numSurp==0:
			#1 guy, no surp
			print possible(totals[0],False,best)
		else:
			#1 guy, surp
			print possible(totals[0],True,best)
	elif numGooglers==2:
		if numSurp==0:
			print possible(totals[0],False,best)+possible(totals[1],False,best)
		elif numSurp==2:
			print possible(totals[0],True,best)+possible(totals[1],True,best)
		elif numSurp==1:
			print max(
				possible(totals[0],True,best)+possible(totals[1],False,best),
				possible(totals[0],False,best)+possible(totals[1],True,best)
			)
	else:
		#numGooglers has to be 3
		if numSurp==0:
			print possible(totals[0],False,best)+possible(totals[1],False,best)+possible(totals[2],False,best)
		elif numSurp==3:
			print possible(totals[0],True,best)+possible(totals[1],True,best)+possible(totals[2],True,best)
		elif numSurp==2:
			print max(
				possible(totals[0],False,best)+possible(totals[1],True,best)+possible(totals[2],True,best),
				possible(totals[0],True,best)+possible(totals[1],False,best)+possible(totals[2],True,best),
				possible(totals[0],True,best)+possible(totals[1],True,best)+possible(totals[2],False,best)
			)
		elif numSurp==1:
			print max(
				possible(totals[0],True,best)+possible(totals[1],False,best)+possible(totals[2],False,best),
				possible(totals[0],False,best)+possible(totals[1],True,best)+possible(totals[2],False,best),
				possible(totals[0],False,best)+possible(totals[1],False,best)+possible(totals[2],True,best)
			)

numCases=int(raw_input())
for i in xrange(1,numCases+1):
	print "Case #%d:"%i,
	nums=map(int,raw_input().split())
	numGooglers=nums[0]
	numSurp=nums[1]
	bestWanted=nums[2]
	googlerPoints=nums[3:]
	case(numGooglers,numSurp,bestWanted,googlerPoints)
