def isThere(x,y):
    x=x.split(" ")
    y=y.split(" ")
    number=0
    sol=0
    for i in x:
        for j in y:
            if(i==j):
                sol=i
                number+=1
    if(number==1):
        return sol
    if(number>1):
        return "Bad magician!"
    if(number==0):
        return "Volunteer cheated!"

with open ("data.txt", "r") as myfile:
    problem=myfile.read()
lines = problem.split('\n')
cases = int(lines[0])
for i in range(cases):
	index = i*10+1
	case=lines[index:index+11]
	first=int(case[0])
	second=int(case[5])
	fline=case[first]
	sline=case[second+5]
	solution=isThere(fline,sline)
	casenum=i+1
	print("case #"+str(i+1)+": " + solution)
