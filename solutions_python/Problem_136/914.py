fin=file("CookieClickerAlphaInput.txt")
fout=file("CookieClickerAlphaOutput.txt","w")
output = ""
T=int(fin.readline().strip())
for t in range(T):
	rate = float(2.0)
	# print fin.readline().strip().split(" ")

	(C,F,X) = [float(x) for x in fin.readline().strip().split(" ")]
	time = 0.0
	while True:
		temp_time1 = X/rate
		temp_time2 = X/(rate+F) + C/rate
		if temp_time2 < temp_time1:
			time += C/rate
			rate += F
		else:
			break
	time += X/rate
	output += "Case #"+str(t+1)+": "+str(round(time,7))+"\n"

fout.write(output)
fout.close()



