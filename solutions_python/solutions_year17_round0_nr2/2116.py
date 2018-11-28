def is_tidy(n):
	return str(n) == ''.join(sorted(str(n)))

def repl(s,i,r):
	ts = list(s)
	ts[i] = r
	return "".join(ts)
	
def tidyfy(number):
	snumber = str(number)
	#print("start" ,snumber)
	for i in range(1,len(snumber)):
		if snumber[i] < snumber[i - 1]:
			snumber = repl(snumber,i-1,str(int(snumber[i-1])-1))
			#print("reduce privious digit" ,snumber)
			for j in range(i,len(snumber)):
				snumber = repl(snumber,j,str(9))
				#print("set next digits to 9" ,snumber)
			break;
	number = int(snumber)
	#print("checking" ,number)
	if not is_tidy(number):
		#print("tidyfying" ,number)
		number = tidyfy(number)
	return number

for t in range(1, int(input()) + 1):
	print("Case #{}: {}".format(t, tidyfy(int(input()))))