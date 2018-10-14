ifile = open("input.txt","r")
nc = int(ifile.readline().replace("\n",""))
ofile = open("output.txt", "w")
for i in range(nc):
    r, k, n = map(int, ifile.readline().replace("\n","").split(" "))
    groups = map(int, ifile.readline().replace("\n","").split(" "))
    index = 0
    amount = 0
    for j in range(r):
	total = 0
	start = index
	while True:
	    total += groups[index]
	    index = (index + 1) % n
	    if index == start:
                break
	    if (total + groups[index] > k):
		break
	amount += total
    ofile.write("Case #" + str(i+1)+ ": " + str(amount) +"\n")

ofile.close()
ifile.close()
	
