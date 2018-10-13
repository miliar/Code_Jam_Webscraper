import math

def isPalindrome(num):
	num = str(num)
	pld = num[::-1]
	if num==pld:
		return True
	else:
		return False

def isSquare(number):
    temp = math.sqrt(int(number))    
    if "." in str(abs(int(temp))):
        return False
    else:
        return True
		
res = 0
no = 1
loop = input()
while loop>0:
	num = raw_input()
	n = num.split(" ")
	start = n[0]
	end = n[1]
	start = int(start)
	end = int(end)
	i = 0
	while i<=end:
		i=i+1
		n = i**2
		if (n)>=start and (n)<=end and isPalindrome(n)==True and isSquare(n)==True and isPalindrome(i)==True:
			res = res+1
	nos = str(no)
	ress = str(res)
	print 'Case #'+nos+': '+	ress
	res = 0
	no = no+1
	loop = loop-1