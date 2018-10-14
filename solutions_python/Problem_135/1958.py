def fun(x,y):
    x=x.split(" ")
    y=y.split(" ")
    n=0
    sol=0
    for i in x:
        for j in y:
            if(i==j):
                sol=i
                n+=1
    if(n==1):
        return sol
    if(n>1):
        return "Bad magician!"
    if(n==0):
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
	solution=fun(fline,sline)
	casenum=i+1
	print("case #"+str(i+1)+": " + solution)
