import sys

def isin(item,mlist):
	try:
		mlist.index(item)
		return True
	except:
		return False

def pairnumber(inf,sup):
	total = 0

	for i in range(inf,sup+1):
		strnum = str(i)
		history = []
		for j in range(1,len(strnum)):
			brother = int(strnum[j:len(strnum)]+strnum[0:j])
			if (brother <= sup and i < brother and not isin(brother,history)):
				history.append(brother)
				total += 1
	return total

number = int(sys.stdin.readline())
myReturn = ""

for i in range(0,number):
	line = sys.stdin.readline()
	inf_sup = line.split()
	myReturn += "Case #"+str(i+1)+": "+str(pairnumber(int(inf_sup[0]),int(inf_sup[1])))+"\n"

print myReturn