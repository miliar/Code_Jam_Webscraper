#!/usr/bin/python

def inp():
	fin=file('in.txt','r')
	fout=file('out.txt','a')
	testCases=fin.readline()
	for count in range(int(testCases)):
		tmp=fin.readline()
		size=tmp.split(" ")
		rows=size[0]
		cols=size[1]
		case=[]
		for row in range(int(rows)):
			case.append(list(fin.readline()))
		result=compute(case,rows,cols)
		out(count,result,fout)

def compute(case,rows,cols):
	row=col=0
	check="true"
	while(row<int(rows) and check=="true"):
		while(col<int(cols) and check=="true"):
			if case[row][col]=="#":
				case[row][col]="/"
				if row==int(rows)-1 or col==int(cols)-1:
					check="false"
					break;
				if case[row][col+1]!="#" or case[row+1][col]!="#" or case[row+1][col+1]!="#":
					check="false"
					break;
				case[row][col+1]="\\"
				case[row+1][col]="\\"
				case[row+1][col+1]="/"
			col=col+1
		col=0
		row=row+1
	if check=="false":
		res=["Impossible","\n"]
		return res
	return case

def out(count,result,fout):
	fout.write("Case #" + str(count+1) + ": " + '\n')	
	for line in result:
		for char in line:
			fout.write(str(char))

def main():
	inp()

main()
