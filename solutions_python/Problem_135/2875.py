import argparse

def Calculate(firstRow,secondRow):
	count = 0
	for fr in firstRow:
		for sr in secondRow:
			if fr == sr:
				temp = fr
				count+=1
	if count==0:
		return "Volunteer cheated!"
	elif count>1:
		return "Bad magician!"
	else:
		return str(temp)

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()
filename = args.filename
f = open(filename,'r')
N = int(f.readline().split("\n")[0])
fout = open("output.txt",'w')
for i in range(1,N+1):
    firstAnswer = int(f.readline().split("\n")[0])
    firstArrangement = [f.readline().split("\n")[0].split(" ") for j in range(0,4)]
    secondAnswer = int(f.readline().split("\n")[0])
    secondArrangement = [f.readline().split("\n")[0].split(" ") for j in range(0,4)]
    fout.write("Case #"+str(i)+": "+Calculate(firstArrangement[firstAnswer-1],secondArrangement[secondAnswer-1])+"\n")
fout.close()