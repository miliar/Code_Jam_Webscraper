filename = "B-large.in"
def fix(number,idx,mult):
	number = number[:idx]+"0"*mult
	newnum = int(number)-1
	return str(newnum)
def findtidy(number):
	flag = True
	if len(number)==1:
		flag = False
	while(flag):
		flag = False
		for i in range(len(number)-1):
			if number[i+1] < number[i]:
				howmany = len(number)-(i+1)
				number = fix(number,i+1,howmany)
				flag=True;
				break;
	return number

with open(filename) as f:
	lines = f.read().split("\n")
	k = int(lines[0])
itr=1
ofile = open("tidyoutputLARGE.txt",'w')
for line in lines[1:-1]:
	tidy = findtidy(line)
	ofile.write("Case #" + str(itr) +": "+tidy+"\n")
	itr+=1
ofile.close()
