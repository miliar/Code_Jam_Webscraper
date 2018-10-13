

def greatest_power_of_10(num):
	div=10
	power = 0
	while((num/div) >=1):
		div*=10
		power+=1
	return power+1

def get_digits(num,place_value):
	digit =num%(10**(place_value+1))-num%(10**place_value)
	return int(digit/(10**(place_value)))

def check_if_tidy(num):
	is_tidy=True
	first_digit = num%10
	second_digit = num//10
	#print('number is '+str(first_digit)+str(second_digit))
	#print('first digit is '+str(first_digit))
	#print('second digit is '+str(second_digit))
	if(first_digit<second_digit):
		is_tidy=False		
	
	return is_tidy
			

def tidy_number(num):


	first_digit = num%10
	#print('Tidy First '+str(first_digit))
	second_digit = num//10
	#print('Tidy Second '+str(second_digit))
	while(num!=0):

		if(not check_if_tidy(num)):
			num-=1
			#print('num is '+str(num))
		else:
			break
	return num



def replace_tidy_number(ori_num,place,tidy_number,size):
	dest_number=tidy_number*(10**place)
	ori_num_seg = (ori_num%(10**(place+size))//(10**place))*(10**place)
	diff = ori_num_seg- dest_number
	new_tidy_num = ori_num - diff
	return new_tidy_num

def pre_process(num):
	power = greatest_power_of_10(num)-1
	new_num = num
	while(power>0):
		gig = get_digits(num,power)
		if(gig==0):
			pre = get_digits(num,power+1)-1
			post = (10**(power+1))-1
			new_num = (pre*(10**(power+1))) + post
			break
		power=power-1

	return new_num



def total_tidy(num):
	power = greatest_power_of_10(num)
	#print('power is '+str(power))
	num = pre_process(num)
	#print('pre processed num '+str(num))
	p=0
	while(p<power):
		first_digit=get_digits(num,p)
		#print('first digit is '+str(first_digit))
		second_digit=get_digits(num,p+1)
		#print('second digit is '+str(second_digit))
		c_num=(10*second_digit)+first_digit
		rep_num = tidy_number(c_num)

		#print('Initial rep num is '+str(rep_num))
		if(int(rep_num%10)>get_digits(num,p-1) and p>0):
			#rep_num=replace_tidy_number(rep_num,0,get_digits(num,p-1),1)
			num = replace_tidy_number(num,p-1,rep_num%10,1)
			#print('SECOND rep_num is '+str(rep_num))
			#print('LOCATION VALUE IS '+str(get_digits(num,p)))
		num = replace_tidy_number(num,p,rep_num,2)
		p=p+1
	return num



t = int(input()) 
for i in range(1, t + 1):
  m = int(input()) 
  print("Case #{}: {}".format(i, total_tidy(m)))
