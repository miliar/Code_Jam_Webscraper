import sys


def acceptable(portions,qta,target):
	target = target*portions

	if target*90 <= qta*100 and qta*100 <= target*110:
		return True
	return False

def findIngr(ingr,ingrPortions,solution,minI,maxI):

	if ingr == len(ingrPortions):
		return solution

	for attempt in ingrPortions[ingr]:
		newMin = max(attempt[0],minI)
		newMax = min(attempt[1],maxI)
		if newMax >= newMin:
			result = findIngr(ingr+1,ingrPortions,solution+[attempt],newMin,newMax)
			if result != None:
				return result

	return None



def solve(N,P,ingr,Q):

	ingrPortions = []

	for n in range(N):
		target = ingr[n]
		ingrPortions.append([])
		for p in range(P):
			qta = Q[n][p]
			minPortions = max(int(qta*10 / (target*11)) - 1,0)
			maxPortions = int(qta*10 / (target*9)) + 1

			for i in range(0,4):
				if acceptable(maxPortions-i, qta, target):
					maxPortions = maxPortions-i
					break
			else:
				continue

			for i in range(0,4):
				if acceptable(minPortions+i, qta, target):
					minPortions = minPortions+i
					break
			else:
				continue

			ingrPortions[n].append((minPortions,maxPortions))

	for i in ingrPortions:
		i.sort(key=lambda a: a[0])

	ingrPortions.sort(key=lambda a: len(a))
	
	count = 0
	for first in ingrPortions[0]:
		result = findIngr(1,ingrPortions,[first],first[0],first[1])
		if result != None:
			count = count + 1
			for i in range(1,len(result)):
				ingrPortions[i].remove(result[i])
	
	return count

t = int(raw_input())
for i in range(1, t + 1):
  N, P = [int(s) for s in raw_input().split(" ")] 

  ingr = [int(s) for s in raw_input().split(" ")]

  Q = []
  for q in range(N):
  	Q.append([int(s) for s in raw_input().split(" ")])


  result = solve(N,P,ingr,Q)
  
  print("Case #{}: {}".format(i, result))

