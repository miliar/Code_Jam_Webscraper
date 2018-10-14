ifile = open("input.txt","r")
nc = int(ifile.readline().replace("\n",""))
lines = ifile.readlines()
lineno = 0
ofile = open("output.txt", "w")
for i in range(nc):
    dataset = map(int,lines[i].replace("\n","").split(" ")[1:])
    a = abs(dataset[1]-dataset[0])
    if len(dataset) >= 3:
	b = abs(dataset[2]-dataset[1])
    else:
	b = 0
    while (a and b):
	if (a>b):
	    a = a%b
	else:
	    b = b%a
    if b:
	a = b
    if (dataset[-1] % a):
        a = a - (dataset[-1] % a)
    else:
        a = 0
    ofile.write("Case #" + str(i+1)+ ": " + str(a) +"\n")

ofile.close()
ifile.close()
	
