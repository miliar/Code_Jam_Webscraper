from math import sqrt

def main():
	input=open("C-small-attempt0.in",'r')
	output=open("3.out","w")
	total=int(input.readline())

	for i in range(1,total+1):
		result=0
		a=input.readline().split(" ")
		x=int(a[0])
		y=int(a[1])
		# print x,y
		for num in range(x,y+1):
			if sqrt(num)==int(sqrt(num)):
				# print num,
				if fair(num)==True:
					# print num,
					# print (int(sqrt(num)))
					if fair(int(sqrt(num)))==True:
						# print num,
						result+=1
						# print result
		
		print "Case #%d: %s" %(i, result)
		output.write("Case #%d: %s\n" %(i, result))

def fair(num):
	numLength=len(str(num))
	for i in range(0, 1+numLength/2):
		if str(num)[i]!=str(num)[-(i+1)] :
			return False
	return True

main()