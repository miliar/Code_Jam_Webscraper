
def isSim(a,b):
	k=a[-1]+a[:-1]
	while(k != a):
		if (k == b):
			return True
		else:
			k=k[-1]+k[:-1]
	return False

def isRec(number,a,b):
	count=0
	for otherNumber in range(number,b+1):
		if isSim(str(number),str(otherNumber)):
			count+=1
		else:
			continue
	return count
def main():
	N=input()
	for i in range(0,N):
		a,b=map(int,raw_input().split(' '))
		count=0
		for number in range(a,b+1):
			case=isRec(number,a,b)
			if case:
				count+=case
			else:
				continue
		print "Case #"+str(i+1)+": "+str(count)
main()
