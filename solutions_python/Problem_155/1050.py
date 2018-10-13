f_in = open("c:/In/A-large.in",'r')
f_out = open("c:/In/A-large.out",'w')
nlines = int(f_in.readline())
for i in range(nlines):
	line_in = f_in.readline()
	lst = line_in.split()
	lst[0] = int(lst[0]) + 1
	lst_sum = [0]*(lst[0])
	lst_req = [0]*(lst[0])
	lst_sum[0] = int(lst[1][0])
	for j in range(lst[0] - 1):
		lst_sum[j+1] = int(lst[1][j+1]) + lst_sum[j]
	lst_req[0] = 0
	for j in range(lst[0] - 1):
		lst_req[j + 1] = j + 1 - lst_sum[j]
	f_out.write("Case #" + str(i + 1) + ": " + str(max(lst_req)) + "\n")
f_in.close()
f_out.close()