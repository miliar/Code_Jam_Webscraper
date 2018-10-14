import math 

def palindrome(num):
	temp = str(num)
	temp2 = temp[::-1]
	return temp == temp2


def fairandsquare(number):

	if not palindrome(number):
		return False
	
	else:
		sqrt = math.sqrt(number)
		int_root = int(sqrt)
		if sqrt != int_root:
			return False
			
		elif palindrome(int_root):
			return True
		else:
			return False



def main():
	
	n = int(raw_input())
	i = 1
	while i <= n:
		
		temp = raw_input().split()
		a = int(temp[0])
		b = int(temp[1])
		j = a
		count = 0
		while j <= b:
			if fairandsquare(j):
				count += 1
			j += 1
		
		tempstr =  "Case #"+ str(i)+": "+str(count)+"\n"
		print tempstr

		
		
		
		i += 1		

main()
