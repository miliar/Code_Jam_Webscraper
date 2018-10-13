f=open(r"D-small-attempt1.in","r")
fo=open(r'outputfile.out',"w")
l1={'1 1 1':'GABRIEL','1 1 2':'GABRIEL','1 1 3':'GABRIEL','1 1 4':'GABRIEL','1 2 1':'GABRIEL','1 2 2':'GABRIEL','1 2 3':'GABRIEL','1 2 4':'GABRIEL','1 3 1':'GABRIEL','1 3 2':'GABRIEL','1 3 3':'GABRIEL','1 3 4':'GABRIEL','1 4 1':'GABRIEL','1 4 2':'GABRIEL','1 4 3':'GABRIEL','1 4 4':'GABRIEL','2 1 1':'RICHARD','2 1 2':'GABRIEL','2 1 3':'RICHARD','2 1 4':'GABRIEL','2 2 1':'GABRIEL','2 2 2':'GABRIEL','2 2 3':'GABRIEL','2 2 4':'GABRIEL','2 3 1':'RICHARD','2 3 2':'GABRIEL','2 3 3':'RICHARD','2 3 4':'GABRIEL','2 4 1':'GABRIEL','2 4 2':'GABRIEL','2 4 3':'GABRIEL','2 4 4':'GABRIEL','3 1 1':'RICHARD','3 1 2':'RICHARD','3 1 3':'RICHARD','3 1 4':'RICHARD','3 2 1':'RICHARD','3 2 2':'RICHARD','3 2 3':'GABRIEL','3 2 4':'RICHARD','3 3 1':'RICHARD','3 3 2':'GABRIEL','3 3 3':'GABRIEL','3 3 4':'GABRIEL','3 4 1':'RICHARD','3 4 2':'RICHARD','3 4 3':'GABRIEL','3 4 4':'RICHARD','4 1 1':'RICHARD','4 1 2':'RICHARD','4 1 3':'RICHARD','4 1 4':'RICHARD','4 2 1':'RICHARD','4 2 2':'RICHARD','4 2 3':'RICHARD','4 2 4':'RICHARD','4 3 1':'RICHARD','4 3 2':'RICHARD','4 3 3':'RICHARD','4 3 4':'GABRIEL','4 4 1':'RICHARD','4 4 2':'RICHARD','4 4 3':'GABRIEL','4 4 4':'GABRIEL'}
T=int(f.readline())
for i in range(T):
	fo.write("Case #"+str(int(i+1))+": "+str(l1[f.readline().rstrip('\n')])+"\n")
fo.close();
