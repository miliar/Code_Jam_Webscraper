import sys
import math
import copy

#palList = []
palList = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L]
def prepare():
        lines = sys.stdin.readlines()
        nbCase = int(lines[0])
        case = {}
        baseLine = 1
        for i in range(nbCase):
                split = lines[1+i].split(' ')
                n = int(split[0])
                m = int(split[1])
                case[i] = (n, m)
        return case


def isPalindrom(number):
	s = str(number)
	middle = len(s) / 2
	for i in range(middle):
		if s[i] != s[len(s)-1-i]:
			return False
	return True

def isPalindromSquare(number):

	s = int(math.sqrt(number))
	if s*s == number:
		if isPalindrom(s):
			return True
	return False


def findNext(number, maxN):

	i = number
	while i <= maxN:
		if isPalindrom(i):
			return i
		i += 1
	return -1


def getPalindroms(number, maxN):
	s = str(number)
	if len(s) % 2 == 1:
		if len(s) == 1:
			maxV = 10
			if maxN < 10:
				maxV = maxN+1
			return range(1,maxV,1)
		else:
			middle = int(len(s) /2)
			res = []
			for i in range(0,10,1):
				tmp = copy.copy(s)
				tmp2 = tmp[:middle] + str(i) + tmp[middle+1:]
				if int(tmp2) > maxN:
					break
				res.append(tmp2)
			return res
				
	else:
		return [number]

	
if __name__ == "__main__":
	'''	
	i = 1
        google = math.pow(10, 100)
        while True:
                p = i * i
                if p > google:
                        break
                if isPalindrom(p) and isPalindrom(i):
                        palList.append(p)
                i += 1
	'''
	
        prep = prepare()
        answer = {}
        for i in prep:
		nb = 0
		for j in palList:
			if j > prep[i][1]:
				break
			elif j >= prep[i][0]:
				nb += 1
		print "Case #" + str(i+1) + ": " + str(nb)
	
	#print palList
