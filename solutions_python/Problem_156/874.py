import copy
import pdb

def serve(pies):
	#pdb.set_trace()
	#initialize the BFS
	maxPie = 0
	init = {}
	for p in pies:
		maxPie = max(maxPie, p)
		if not p in init: init[p] = 0
		init[p] += 1

	if maxPie <= 3: return maxPie 

	#setting queue.
	queue = []	
	queue.append({'distribution': init, 'max': maxPie, 'time': 0})

	#start BFS
	while len(queue):
		#get the current status
		current = queue[0]
		maxPie = current['max']
		currentTime = current['time']
		if maxPie <= 2: return currentTime + maxPie 

		queue.pop(0)

		#not calling the special time
		distribution = copy.copy(current['distribution'])
		tmpMax = 0 
		for i in range(1, maxPie+1):
			if i in distribution:
				tmpMax = i-1
				distribution[i-1] = distribution[i]
		del(distribution[maxPie]) #clear the maximal pie
		if tmpMax > 1: # more than 2!
			# push this status into the queue
			queue.append({'distribution': distribution, 'max': tmpMax, 'time': currentTime+1})
		else: return 2 + current['time'] 
		#pdb.set_trace()

		#calling the special time if the remaining maximal pie is more than 1
		for k in range(1, maxPie / 2+1):
			half = maxPie - k
			distribution_s = copy.copy(current['distribution'])
			distribution_s[maxPie] -= 1
			if distribution_s[maxPie] == 0: del(distribution_s[maxPie])
			if not half in distribution_s: distribution_s[half] = 0
			distribution_s[half] += 1
			if not maxPie-half in distribution_s: distribution_s[maxPie-half] = 0
			distribution_s[maxPie-half] += 1
			tmpMax = 1
			for i in range(maxPie):
				if maxPie-i in distribution_s:
					tmpMax = maxPie-i
					break 
			queue.append({'distribution': distribution_s, 'max':tmpMax, 'time': currentTime+1})
		#pdb.set_trace()

	return 2000

def main():
	
	f = open('B-small-attempt2.in')
	result = open('bb-result-1.txt', 'w')
	testcount = int(f.readline())
	for i in range(testcount):
		d = int(f.readline())
		pies = [int(p) for p in (f.readline()).split(' ')]
		minimal = serve(pies) 
		result.write('Case #%d: %d\n' % (i+1, minimal))	
		print i, ' ', pies, ' ', minimal
			
	print serve([4])
	print serve([5])
	print serve([1,2,1,2])
	print serve([3])
	print serve([8,4,2,3,1])
main()
