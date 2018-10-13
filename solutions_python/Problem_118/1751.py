import math

def isPalin(no):
	res = no
	no = no
	rev = 0
	while(no != 0)  :
		rev = rev*10 + no%10
		no = no/10
	return rev == res

count = 0
result = ""
INPUT = open("./C-small-attempt0.in","r")
T = long(INPUT.readline())
for loop in range(T) :
	count = 0
	temp = INPUT.readline()
	A = long(temp[:temp.find(' ')])
	B = long(temp[temp.find(' '):len(temp)])

	for i in range(A,B+1) :
		if isPalin(i) == False :
			continue
		if math.sqrt(i) == long(math.sqrt(i)) :
			if isPalin(long(math.sqrt(i))) :
				count += 1

	result = result + "Case #" + str(loop+1) + ": " + str(count) + "\n"
	OUTPUT = open("./output.txt","w")
	OUTPUT.write(result)
	OUTPUT.close()	

INPUT.close()