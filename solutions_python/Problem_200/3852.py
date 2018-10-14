import os
def WriteFile(b,a):
	f= open(a,"w+")
	for line in b:
		f.write(line+"\n")
	f.close

def ReadFile(a):
	return([line.rstrip('\n') for line in open(a)])


def reverse(strs):
    for i in xrange(len(strs)-1, -1, -1):
        yield strs[i]
 
def make_case(d):
	for i in range(len(d)):
		d[i] = "Case #" + str(i+1) + ": " + d[i]
	return(d)
	

FileIn = 'B-small-attempt5.in'
lines = ReadFile(FileIn)
del lines[0]
l=[]
def maincode():
	for line in lines:
		ListOfInts = list(map(int,line))
		#ListOfInts[-1:] = 9
		SortedList = sorted(ListOfInts)
		if SortedList != ListOfInts:
			for i in range(1,len(ListOfInts)):
				if ListOfInts[i-1] >= ListOfInts[i]:
					print(ListOfInts)
					print(ListOfInts[i-1])
					ListOfInts[i-1] -= 1
					for a in range(i,len(ListOfInts)):
						ListOfInts[a] = 9
					break
		
		l.append(''.join(str(e).strip("0") for e in ListOfInts))
maincode()
print(l)
l = make_case(l)
WriteFile(l,'B-small-attempt5.out')
