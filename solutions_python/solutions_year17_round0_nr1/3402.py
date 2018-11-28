import os
def WriteFile(b,a):
	f= open(a,"w+")
	for line in b:
		f.write(line+"\n")
	f.close

def ReadFile(a):
	return([line.rstrip('\n') for line in open(a)])


def Positives(pancakes):
  groupedHeight = pancakes.count('+')
  return groupedHeight
 
def make_case(d):
	for i in range(len(d)):
		d[i] = "Case #" + str(i+1) + ": " + d[i]
	return(d)
	

FileIn = 'A-large.in'
lines = ReadFile(FileIn)
l=[]
def maincode():
	for line in lines:
		a,n = line.split(' ', 1)
		n = int(n)
		i=0
		print(line)
		for m in range(len(a)):
			if a[m] == "-":
				tempstr = a[m:m+n]
				tempstr = tempstr.replace("+","a")
				tempstr = tempstr.replace("-","+")
				tempstr = tempstr.replace("a","-")
				i+=1
				a = a.replace(a[m:m+n],tempstr,1)
				print(a)
				print(n)
			print(len(a))
			print(m+n)
			if len(a) < m+n+1 and (a[n*-1-1:].find("+-") != -1 or a[n*-1-1:].find("+-") != -1):
				l.append("IMPOSSIBLE")
				print("NEXT IM")
				break
			elif len(a) == Positives(a):
				l.append(str(i))
				print("NEXT")
				break
			
			#os.system("pause")
maincode()
print(l)
l = make_case(l)
WriteFile(l,'A-large.out')
