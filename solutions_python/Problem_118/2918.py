import math

f = open("C-small-attempt0.in")
ar = f.read().split("\n")

numberofcases = ar[0]
x = ar[3].split(" ")[0]
y = ar[3].split(" ")[1]

def ispalindrom(z):
	lenght = len(z)
	if 1>=lenght:
		return True
	else:
		if z[0]==z[-1]:
			#print z[1:-1]
			return ispalindrom(z[1:-1])
		else:
			return False

def sq(z):
	if 0 != math.sqrt(z)%1:
		return False
	else:
		return True

def fromtill(x,y):
	s=x
	z=y
	count=0
	while s<=z:
		if ispalindrom(str(s)):
			if sq(s):
				if ispalindrom(str(int(math.sqrt(s)))):
					#print s
					count+=1
		s+=1
	return count

def cases():
	i=1
	while i <= int(numberofcases):
		x = ar[i].split(" ")[0]
		y = ar[i].split(" ")[1]
		p= fromtill(int(x),int(y))
		print "Case #" + str(i) + ": " + str(p)
		i+=1

cases()