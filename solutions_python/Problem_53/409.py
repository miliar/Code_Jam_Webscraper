ifile = open("input.txt","r")
nc = int(ifile.readline().replace("\n",""))
ofile = open("output.txt", "w")
for i in range(nc):
    n, k = map(int, ifile.readline().replace("\n","").split(" "))
    if ( (k % (2 ** n)) == (2 ** n - 1) ):
	ofile.write("Case #" + str(i+1)+ ": ON\n")
    else:
        ofile.write("Case #" + str(i+1)+ ": OFF\n")

ofile.close()
ifile.close()
	
