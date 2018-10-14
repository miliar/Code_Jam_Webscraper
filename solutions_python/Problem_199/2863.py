num= int( input( ) )


for i in range(num):
	line, k = input().split(" ")
	k = int(k)
	works=True
	cnt=0
	#j=0
	# while j!= len(line):=
	for j in range( len(line)-k+1 ):
		#print(str(j)+ " line j: "+ line[j]+ " total line: "+line)
		if line[j]=='-':
			cnt+=1
			for l in range(k):
				if line[j+l] =='+':
					newline=line[:j+l] + '-' +line[j+l+1:]
					line=newline
				else:
					newline=line[:j+l] + '+' +line[j+l+1:]
					line=newline
	#print("end result:" + line)


	for j in line:
		if j =='-':
			works=False

	if works:
		print("Case #{}: {}".format(i+1, cnt))
	else:
		print("Case #{}: IMPOSSIBLE".format(i+1) )

