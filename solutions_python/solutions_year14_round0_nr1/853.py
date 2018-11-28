f = open("./dataset", "rb")
ofp = open("./output", "wb")

cases = int(f.readline())

for N in range(0, cases, 1):

	row1 = int(f.readline())

	for i in range(0, 4, 1):
		if(i==row1-1):
			rowElements1 = [int(x) for x in f.readline().split()]
		else:
			f.readline()


	row2 = int(f.readline())
        for i in range(0, 4, 1):
               if(i==row2-1):
                       rowElements2 = [int(x) for x in f.readline().split()]
               else:
                       f.readline()



	ans = [x for x in (set(rowElements1) & set(rowElements2))]
	if(len(ans) == 1):
		ofp.write("Case #"+str(N+1)+": "+str(ans[0])+"\n")
	else:
		if(len(ans) > 1):
			ofp.write("Case #"+str(N+1)+": Bad magician!"+"\n")
		else:
			ofp.write("Case #"+str(N+1)+": Volunteer cheated!"+"\n")

f.close()
ofp.close()
