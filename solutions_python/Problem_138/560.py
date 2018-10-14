import os
import sys

def SmallestWeightIndex(blocks):
	index = 0
	for i in range(1, len(blocks)):
		if (blocks[i] < blocks[index]):
			index = i
	return index

def LargestWeightIndex(blocks):
	index = 0
	for i in range(1, len(blocks)):
		if (blocks[i] > blocks[index]):
			index = i
	return index

def NextLargestWeightIndex(blocks, weight):
	index = -1
	for i in range(0, len(blocks)):
		if blocks[i] > weight and (index == -1 or blocks[i] < blocks[index]):
			index = i
	return index if index != -1 else SmallestWeightIndex(blocks)

def War(naomi, ken):
	pointsNaomi = 0
	pointsKen = 0
	while(len(naomi) > 0):
		naomiLargest = LargestWeightIndex(naomi)
		kenSmallest = SmallestWeightIndex(ken)
		kenLargest = LargestWeightIndex(ken)

		naomiChosen = naomiLargest
		kenChosen = NextLargestWeightIndex(ken, naomi[naomiChosen])

		if naomi[naomiChosen] > ken[kenChosen]:
			pointsNaomi += 1
			naomi.pop(naomiChosen)
			ken.pop(kenChosen)
		else:
			pointsKen += 1
			naomi.pop(naomiChosen)
			ken.pop(kenChosen)
	return pointsNaomi

def DeceitfulWar(naomi, ken):
	pointsNaomi = 0
	pointsKen = 0
	while(len(naomi) > 0):
		naomiSmallest = SmallestWeightIndex(naomi)
		naomiLargest = LargestWeightIndex(naomi)
		kenSmallest = SmallestWeightIndex(ken)
		kenLargest = LargestWeightIndex(ken)

		naomiChosen = naomiSmallest
		kenChosen = kenSmallest
		naomiToldWeight = naomi[naomiChosen]

		if ken[kenChosen] < naomi[naomiChosen]:
			pointsNaomi += 1
		else:
			kenChosen = kenLargest
			pointsKen += 1


		'''
		if naomi[naomiChosen] < ken[kenLargest]:
			#naomiChosen = naomiSmallest
			naomiToldWeight = ken[kenLargest] - 0.0000001
			#kenChosen = NextLargestWeightIndex(ken, naomiToldWeight)
			kenChosen = kenLargest
			pointsKen += 1
		else:
			naomiToldWeight = naomi[naomiChosen]
			#kenChosen = NextLargestWeightIndex(ken, naomiToldWeight)
			kenChosen = kenSmallest
			pointsNaomi += 1
		'''

		#print(str(naomi[naomiChosen]) + ", " + str(ken[kenChosen]))
		naomi.pop(naomiChosen)
		ken.pop(kenChosen)
	#print("P: " + str(pointsNaomi) + " " + str(pointsKen))		
	return pointsNaomi


t = int(input())
dif = 0.000000001
for ti in range(1, t+1):
	n = int(input())
	naomi = input().split()
	ken = input().split()
	for i in range(0, n):
		naomi[i]= float(naomi[i])
		ken[i] = float(ken[i])
	#print(naomi)
	#print(ken)
	pointsD = DeceitfulWar(naomi[:], ken[:])
	pointsW = War(naomi[:], ken[:])
	print("Case #" + str(ti) + ": " + str(pointsD) + " " + str(pointsW))
