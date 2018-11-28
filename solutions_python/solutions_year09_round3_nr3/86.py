'''
Created on Sep 13, 2009
@author: namnx
'''
import sys
INFILE = 'prob3-small.in'
OUTFILE = 'prob3-small.out'

def countCoins(start, end, cells):
	if len(cells) == 1:
		return end - start
	d1 = cells[0] - start
	d2 = end - cells[-1]
	if d1 > d2:
		newStart = cells[0] + 1
		cells.remove(cells[0])
		return end - start + countCoins(newStart, end, cells)
	newEnd = cells[-1] - 1
	cells.remove(cells[-1])
	return end - start + countCoins(start, newEnd, cells)


def calCost(status, cells):
	start = cells[0] - 1
	end = cells[0] + 1
	while (status[start] == True): start -=1
	while (status[end] == True): end +=1
	if len(cells) == 1:
		return end - start -2
	
	cost = sys.maxint
	for i in range(len(cells)):
		statusi = list(status)
		cellsi = list(cells)
		costi = calCost(status, [cellsi[i]])
		statusi[cells[i]] = False
		cellsi.remove(cells[i])
		costi += calCost(statusi, cellsi)
		if costi < cost:
			cost = costi
	return cost


def main():
	fin = file(INFILE, 'r')
	fout = file(OUTFILE,'w')
	n = int(fin.readline())
	for i in range(n):
		line = fin.readline().strip()
		p,q = line.split()
		p = int(p)
		q = int(q)
		line = fin.readline().strip()
		cells = line.split()
		for j in range(len(cells)): 
			cells[j] = int(cells[j])
		status = [False]
		for j in range(p):
			status.append(True)
		status.append(False)
		numCoins = calCost(status, cells)
		fout.write('Case #' + str(i+1) + ': ' + str(numCoins) + '\n')
		
	fin.close()
	fout.close()
	
	
if __name__ == '__main__':
	main()
#	status = [False]
#	for i in range(0,20):
#		status.append(True)
#	status.append(False)
#	print calCost(status, [3,6,14])
	#print countCoins(1, 20, [3,6,14])