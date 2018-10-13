def tidy_numbers():
	t = long(raw_input())
	prev_high=0
	for i in range(0, t):
		n = long(raw_input())
		j= 0
		while(str(j)!=str(n)):
			j+=1
			digits = str(j)
			if(is_increasing(digits)):
				prev_high = long(digits)
			
		print("Case #"+str(i+1)+": "+str(prev_high))



def is_increasing(digits):
	
	if(len(digits)==1):
		return True
	if(len(digits)==2):	
		if(digits[1]<digits[0]):
			return False
		else:
			return True
	i=0
	while(long(i)<len(digits)-1):
		if(long(digits[i+1])<long(digits[i])):
			return False
		i = long(i) + 1
		
	return True


if __name__ == "__main__":
    tidy_numbers()




