import sys

sys.setrecursionlimit(15000)
infile = sys.argv[1]
outfile = sys.argv[2]

inf = open(infile)
outf = open(outfile, 'w')

def merge(list1, list2):
	newlist = []
	while (len(list1) > 0 and len(list2) > 0):
		if list1[0] <= list2[0]:
			newlist += [list1[0]]
			list1 = list1[1:]
		else:
			newlist += [list2[0]]
			list2 = list2[1:]
	newlist += list1+list2
	return newlist

def mergeSort(array):
	sortedarray = []
	if len(array) > 1:
		sortedarray = merge(mergeSort(array[:len(array)/2]), mergeSort(array[len(array)/2:]))
	else:
		sortedarray = array
	# print len(sortedarray)
	return sortedarray

def war(array1, array2): #takes in two sorted arrays
	kens_score = 0
	pointer = 0
	for i in range(0, len(array1)):
		for j in range(pointer, len(array2)):
			if array2[j] > array1[i]:
				kens_score += 1
				pointer = j+1
				break
		if pointer == len(array2):
			break
	return len(array1) - kens_score

# def dwar(array1, array2):
# 	possible_scores = []
# 	for i in range(0, len(array1)):

def dwar(array1, array2):
	noamis_score = 0
	# for i in range(0, len(array1)):
	if len(array1) == 0 or len(array2) == 0:
		return noamis_score
	if array1[0] > array2[0]:
		# print 'entering more loop'
		# print array1[i+1:]
		# print array2[i+1:]
		noamis_score += 1 + dwar(array1[1:], array2[1:])
		# break
	else:
		# print 'entering less loop'
		# print array1[i+1:]
		# print array2[:-i-1]
		noamis_score += dwar(array1[1:], array2[:-1])
	return noamis_score

def d_war(array1, array2):
	kens_score = 0
	numofhits = 0
	for i in range(0, len(array1)):
		if array1[i] < array2[0]:
			kens_score += 1
		else:
			numofhits = len([x for (x, y) in zip(array1[i:], array2[:-i]) if x > y])
			break
	return numofhits#len(array1) - kens_score
def dewar(array1, array2):
	noamis_score = 0
	kens_score = 0
	noamis_pointer = len(array1) - 1
	kens_pointer = len(array2) - 1
	while (kens_pointer >= noamis_score and noamis_pointer >= kens_score):#noamis_score + kens_score < len(array1)):
	# for i in range(0, len(array1)):
	# 	for j in range(backpointer, len(array2)):
			if array1[noamis_pointer] > array2[kens_pointer]:
				noamis_score += 1
				noamis_pointer -= 1
				# backpointer = j+1
				# break
			else:
				subscore = war(array1[len(array1)-kens_pointer:], array2[:kens_pointer])
				# if subscore 
				# kens_score += 1
				# kens_pointer -= 1
				# backpointer = j+1
				# break
	return noamis_score
	# kens_score = 0
	# backpointer = len(array2)-1
	# pointer = 0
	# for i in range(0, len(array2)):
	# 	for j in range(pointer, len(array1)):
	# 		if array2[len(array2)-1-i] > array1[j]:
	# 			pointer += j+1#1
	# 			kens_score += 1
	# 			break
	# 	if pointer == len(array1):
	# 		break
	# print array1[pointer:]
	# print array2[:len(array2)-pointer]
	# noamis_score = war(array1[pointer:], array2[:len(array2)-pointer])
	# return noamis_score #len(array1) - kens_score
		# noamis_score += war(array1[pointer+1:], array2[:backpointer])

	# return len([x for (x, y) in zip(array1, array2)])
def readTestCase(num):
	numBlocks = int(inf.readline())
	naomi = mergeSort([float(x) for x in inf.readline().split()])
	# print naomi
	ken = mergeSort([float(x) for x in inf.readline().split()])
	# print ken
	noami_plays_war = str(war(naomi, ken))
	noami_plays_dwar = str(dwar(naomi, ken))
	outf.write('Case #' + num + ': ' + noami_plays_dwar + ' ' + noami_plays_war + '\n')
	#sort the arrays

numTestCases = inf.readline()

for i in range(0, int(numTestCases)):
	readTestCase(str(i+1))