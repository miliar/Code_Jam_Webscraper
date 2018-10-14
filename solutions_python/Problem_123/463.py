import sys
import math
import re


def case():

	A, N = (int(x) for x in input().split(' '))

	motes = [int(x) for x in input().split(' ')]

	motes.sort()
	addpopList = []

	cnt = 0
	#print (A, motes)

	while (motes):

		#print (motes)

		if A > motes[0]:
			A += motes.pop(0)
			#print ('easy', A)
		elif A <= motes[0]:
			popcnt = len(motes)
			addcnt = 0
			tmpA = A
			#print ('A', A, 'popcnt', popcnt)
			while motes and (tmpA <= motes[0]):
				if tmpA == 1:
					addcnt = popcnt + 1
					break
				tmpA += (tmpA - 1)
				addcnt += 1

			if addcnt < popcnt:
				cnt += addcnt
				A = tmpA
			else:
				cnt += popcnt
				motes = []

			addpopList.append([addcnt, popcnt, addcnt])


	i = len(addpopList)-1
	if i >= 0 and (addpopList[i][2] > addpopList[i][1]):
		addpopList[i][2] = addpopList[i][1]
	i -= 1

	while i >= 0:
		if (addpopList[i][2] > addpopList[i][1]):
			addpopList[i][2] = addpopList[i][1]

		addpopList[i][2] += addpopList[i+1][2]

		if (addpopList[i][2] > addpopList[i][1]):
			addpopList[i][2] = addpopList[i][1]

		i -= 1

	if addpopList:
		cnt = addpopList[0][2]
	#print (addpopList) 


	sys.stdout.write(str(cnt))





if __name__=="__main__":

	if len(sys.argv) > 1:
		sys.stdin = open(sys.argv[1])

	num_cases = int(input())

	for c in range (1, num_cases+1):
		sys.stdout.write('Case #')
		sys.stdout.write(str(c))
		sys.stdout.write(': ')
		case()
		sys.stdout.write('\n')
