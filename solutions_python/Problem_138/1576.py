import sys 

def binSearch(val, l):
	lb, rb = 0, len(l)-1
	if val < l[0]:
		return 0
	if val > l[rb]:
		return 0
	while rb - lb > 1:
		mid = (lb + rb) / 2	
		if val > l[mid]:
			lb = mid
		elif val < l[mid]:
			rb = mid
	return rb				

def kensBestResp(a, kensList):
	#resp = kensList[binSearch(a, kensList)]
	idx = binSearch(a, kensList)
	resp = kensList[idx]
	del kensList[idx]
	return resp

def playWar(nlist, klist):
	naomiPts = 0
	for block in nlist:
		if kensBestResp(block, klist) < block:
			naomiPts +=1
	return naomiPts		

def getSuitableBlock(nlist, klist):
	for block in nlist:
		greater = [x for x in klist if x > block] 	
		lesser =  [x for x in klist if x < block] 	
		if len(greater) > 0 and len(lesser) > 0:
			return block, greater
	return None, None
# rule for deceit: if N has a blk st K has a block greater and a block less than...
def playDWar(nlist, klist):
	naomiPts = 0
	while len(nlist) > 0:
		suitableBlock, greater = getSuitableBlock(nlist, klist)
		if suitableBlock is not None:
			if kensBestResp(max(greater) + 0.00000001, klist) < suitableBlock:
				naomiPts +=1 
				nlist.remove(suitableBlock)
		else:
			block = nlist[0]
			if kensBestResp(block, klist) < block:
				naomiPts +=1
			nlist.remove(block)
	return naomiPts		
					
				
	

			
def getWarInput(fyle):
	f = open(fyle)
	numCases = int(f.readline())
	for i in range(numCases):
		n = int(f.readline())
		nlist = [float(x) for x in f.readline().split()]
		nlist = sorted(nlist)
		klist = [float(x) for x in f.readline().split()]
		klist = sorted(klist)
		naomiPts = playWar(nlist[:], klist[:])
		naomiPtsD = playDWar(nlist[:], klist[:])
		print 'Case #%s: %i %i' %(i+1, naomiPtsD, naomiPts)
								
if len(sys.argv) != 2:
	print "Here's the format: <thisfilename.py> <inputstuff>  , Try again."
else:
	phile = sys.argv[1]
	getWarInput(phile)		
		
	
	
	
	
	
