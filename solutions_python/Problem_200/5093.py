t = int(input())
def check_ascending(number):
	if number==int(''.join(sorted(list(str(number))))):
		return True 
	else:
		return False			
for case in range(t):				
	number = int(input())
	while True:
		if check_ascending(number):
			print("Case #{}: {}".format(case+1, number))
			break
		else:
			number-=1

