def displaypeople(string):
	count=0
	peopleneeded=0
	people=0
	while count<len(string):
		if people<count:
			peopleneeded+=count-people
			people=count
		if people>=count and int(string[count])>0:
			people+=int(string[count])
		count+=1
	return peopleneeded

def main():
	count=0
	writefile = open("C:/Users/Akash/Desktop/output.in","w")
	with open("C:/Users/Akash/Desktop/A-large.in") as fileobject:
		for line in fileobject:
			line=line.rstrip('\n')
			if count==0:
				testcase=int(line)
			else:
				string = line.split(" ")[1]
				peopleneeded=0
				peopleneeded=displaypeople(string)
				writefile.write("Case #"+str(count)+ ": "+str(peopleneeded)+"\n")
			count+=1
main()
