from collections import Counter
times = 0;
times = int(raw_input())
for magic in range(0,times):
	rows = []
	for steps in range(0,2):	
		row = []
		answ = int(raw_input())
		for line in range(0, 4):
			if(line==answ-1):	
				tmp = raw_input().split(" ")
				for colum in range(0, 4):
					row.append(int(tmp[colum]))
				rows.append(row)		
			else:
				raw_input()
	some = list((Counter(rows[0]) & Counter(rows[1])).elements())
	result = len(some)
	if(result==0):
		print("Case #%d: Volunteer cheated!" %(magic+1))
	elif(result==1):
		print("Case #%d: %d" %(magic+1, some[0]))
	elif(result>1):
		print("Case #%d: Bad magician!" %(magic+1))
	

