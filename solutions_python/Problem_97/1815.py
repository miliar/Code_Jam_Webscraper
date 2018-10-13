# Define a main() function
def main():
    recNumFile= open("C-small-attempt0.in","r")
    numOfCases = recNumFile.readline() 
    for (index,line) in zip(range(int(numOfCases)),recNumFile):
	print "Case #"+ str(index + 1)+": " + str(get_recycled_num(int(line.split(" ")[0]),int(line.split(" ")[1])))
	

def get_recycled_num(rangStart,rangEnd):
    numList=[]
    cyclicPer = []
    recNumCount =[] 
    for num in range(rangStart,rangEnd+1):
	numList.append(str(num))
    while numList:
	curntNum = numList.pop()
	cyclicPerm = get_cyclic_perm(curntNum)
	for num in cyclicPerm:
	    if num in numList:
		if not (curntNum,num) in recNumCount:
		    recNumCount.append((curntNum,num))
    return len(recNumCount)

def get_cyclic_perm(aNum):
    permList = []
    aPerm = ''
    for i in range(len(aNum)):
	aPerm = aNum[i:] + aNum[:i]
	while aPerm[0] == '0':
	    aPerm = aPerm[1:]
	if i:
	    permList.append(aPerm)
    return permList

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
