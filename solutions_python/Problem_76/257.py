import math
def xoruj(tab):
	wyn = tab[0]
	for x in tab[1:]:
		wyn = wyn^x
	return wyn

def silnia(i):
	wyn = 1
	for x in range(2,i+1):
		wyn*=x
	return wyn

def doSth(a):
	maxim = -1
	for x in range(1,-1+int(math.pow(2,(len(a))))):
		licz =  [int(x) for x in list(bin(x)[2:].zfill(len(a)))]
		patric = []
		sean = []
		for l in range(len(a)):
			if(licz[l]==1):
				patric.append(a[l])	
			else:
				sean.append(a[l])
		maxim = max(compare(sean,patric),maxim)
	if(maxim==-1):
		print "NO"
	else:
		print maxim

def compare(sean,patric):
	if(xoruj(sean)==xoruj(patric)):
		return max(sum(sean),sum(patric))

a = [1,2,3,4,5]
N = int(raw_input())
for t in range(N):
	M = int(raw_input())
	nums = [int(x) for x in raw_input().split()]
	#print nums
	print "Case #"+str(t+1)+":",
	doSth(nums)


