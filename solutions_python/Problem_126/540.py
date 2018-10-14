import re

def substr(string):
    j=1
    a=[]
    while True:
        for i in range(len(string)-j+1):
            a+=[string[i:i+j]]
        if j==len(string):
            break
        j+=1
    return a

def check(s,n):
	l=re.findall(r"[bcdfghjklmnpqrstvwxyz]+",s)
	for st in l:
		if(len(st)>=n):
			return 1
	return 0

def nvalue(s,n):
	counter=0
	l=substr(s)
	for st in l:
		if(check(st,n)==1):
			counter+=1

	return counter

t=input()
for i in range(1,t+1):
	inp=raw_input()
	print "Case #"+str(i)+":",nvalue(inp.split(" ")[0],int(inp.split(" ")[1]))
