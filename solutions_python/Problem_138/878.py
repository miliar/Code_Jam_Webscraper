fin=file("DeceitFulWarInput.txt")
fout=file("DeceitFulWarOutput.txt","w")
output = ""
T=int(fin.readline().strip())
for t in range(T):
	print "Case"+str(t+1)
	N = int(fin.readline().strip())
	naomi = [float(x) for x in fin.readline().strip().split(" ")]
	naomi2 = [x for x in naomi]
	ken = [float(x) for x in fin.readline().strip().split(" ")]
	ken2 = [x for x in ken]
	naomi.sort()
	naomi2.sort()
	ken.sort()
	ken2.sort()
	print ken2
	print naomi2
	print "-----"
	while True:
		#Remove minimum element from naomi and maximum element from ken
		if len(naomi2) == 0:
			break
		if naomi2[0] > ken2[-1]:
			break
		flag = 0
		for i in range(len(naomi2)):
			if naomi2[i] > ken2[i]:
				flag+=1
		if flag == len(naomi2):
			break
		naomi2.remove(naomi2[0])
		ken2.remove(ken2[-1])
	print ken2
	print naomi2
	win_deceit = len(ken2)
	i = 0
	win = 0
	while i<len(naomi):
		temp_list = [x for x in ken if x>naomi[i]]
		temp_list.sort()
		if len(temp_list) > 0:
			ken.remove(temp_list[0])
		else:
			win+=1
		i+=1
	print "Case #"+str(t+1)+": "+str(win_deceit)+" "+str(win)+"\n"
	print "========================="
	output += "Case #"+str(t+1)+": "+str(win_deceit)+" "+str(win)+"\n"
	# if win!=N:
	# 	output += "Case #"+str(t+1)+": "+str(N-1)+" "+str(win)+"\n"
	# else:
	# 	output += "Case #"+str(t+1)+": "+str(N)+" "+str(win)+"\n"

fout.write(output)
fout.close()



