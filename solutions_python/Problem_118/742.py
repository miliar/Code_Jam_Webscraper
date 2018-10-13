import math,time

def is_palindrome(n):
    x=str(n)
    y=x[::-1]
    if x != y:
        return False
    return True

up_limit = 1e14
x=int(up_limit ** (0.5))

l = [0]
counter = 0
for i in range(1,x+1):
    if is_palindrome(i) == True:
        if is_palindrome(i*i) == True:
        	counter += 1
    l.append(counter)

def count(A,B):
	AA= int(math.ceil(A**(0.5)))
	BB= int(B**(0.5))
	return l[BB]-l[AA-1]
	
thefile = "C-large-1"
outputfile=open(thefile + ".out","w")

with open(thefile + ".in") as f:
	ff = [[int(x) for x in line.split()] for line in f]
	
for i in range(1,ff[0][0]+1):
	outputfile.write("Case #%i: %i\n" % (i,count(ff[i][0],ff[i][1])))
	



