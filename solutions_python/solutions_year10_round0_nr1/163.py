f=open('C:/Users/Meir/python/codejam/Cinput1.txt', 'r')
g=open('C:/Users/Meir/python/codejam/Coutput1.txt', 'w')	
Length=0
Dictsize=0
TestSize=0

aline=f.readline()
bline=aline.split(" ")

Testsize=int(bline[0])

for idx in range(Testsize):
	aline=f.readline()
	bline=aline.split(" ")
	snappers=int(bline[0])
	snaps=int(bline[1])
	res='ON'
	for idx2 in range(snappers):
		if(snaps % 2==0):
			res='OFF'
			break
		else:
			snaps/=2
	g.write("Case #" + str(idx+1)+": " + res+"\n")
			

	 
