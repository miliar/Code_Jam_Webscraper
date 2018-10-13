def isTidy(string):
	# return string==''.join(x for x in sorted(list(string)))
	init = string[0];
	check = True;
	for i in string[1:]:
		if (i!=init):
			if (i>init):
				init=i;
				check = check and True;
			else:
				check = False;

	return check;

def returnTidy(number):
	if isTidy(str(number)):
		return number;
	# return False;
	else:

		return returnTidy(number-1);
		# return returnTidy(str(int(string)-1));
# print (isTidy("12345"))
def iterativeTidy(number):
	for x in range(number,0,-1):
		if isTidy(str(x)):
			return x;

if __name__ == "__main__":
	# print (open("A-small.in").readline().strip(), end='')
	# inputs = [];
	f = open("B-small-attempt1.in");
	for i in range(0,int(f.readline().strip())):
		eachInput = f.readline().strip();
		print ("Case #"+str(i+1)+ ": " + str(iterativeTidy(int(eachInput))))
		# print (str(int(returnTidy(eachInput))-1))
		
