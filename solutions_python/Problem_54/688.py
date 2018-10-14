import sys
import string
#import fractions

sys.stdout.softspace = 0




def gcd(a,b):
	"""Return greatest common divisor using Euclid's Algorithm."""
	while b:      
		a, b = b, a % b
	return a


# the function to calculate the GCD
def gcd1(num1, num2):
    result = 1
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1 * num2 / num1
        return result


def ReadData(fileName):
	f = open(fileName, "rb")

	C = int(f.readline())

#	for line in f:
	for i in range(1, C + 1):
		line = f.readline()
		lineList = string.split(line, " ")
		N = int(lineList[0])

		#print "N = ", N,

		t = []
		for j in range(1, N + 1):
			#print int(lineList[j]),
			t.append(int(lineList[j]))
		#print
		#print "t = ", t,

		diffT = []
		for j in range(0, N):
			for k in range(j + 1, N):
				diffT.append(abs (t[j] - t[k]))

				'''
				if (j != k):
					if (t[j] < t[k]):
						diffT.append(t[k] - t[j])
					else:
						diffT.append(t[j] - t[k])
				'''

		#print "diffT = ", diffT

		#T = GCD(diffT)
		T = diffT[0]
		for j in range(1, len(diffT)):
			#T = fractions.gcd(T, diffT[j])
			T = gcd(T, diffT[j])

		#print "GCD = ", T

		#y is the biggest of the smallest value to add to make all t[] multiple of T
		max = 0
		for j in range(0, N):
			remainder = t[j] % T
			
			if (remainder > 0):
				if (max < T - remainder):
					max = T - remainder

		y = max

		print "Case #%d: %d" % (i, y)
		
#	f = open("B.in", "rb")
#	data = f.read()
#	f.close()



#ReadData("B.in")
#ReadData("B-small-attempt0.in")
#ReadData("B-small-attempt1.in")
ReadData("B-large.in")
