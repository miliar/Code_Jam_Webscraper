x=int(raw_input())
def check(list):
	for i in range(0,4):
		count=0;
		for j in range(0,4):
			if list[i][j]=="X" or list[i][j]=="T":
				count=count+1;
			if count==4:
				return 1;
		count=0;
		for j in range(0,4):
			if list[i][j]=="O" or list[i][j]=="T":
                	        count=count+1;
	                if count==4:
				return 2;
		count=0;
		for j in range(0,4):
			if list[j][i]=="X" or list[j][i]=="T":
                                count=count+1;
                        if count==4:
                                return 1;
                count =0;
		for j in range(0,4):
                        if list[j][i]=="O" or list[j][i]=="T":
                                count=count+1;
                        if count==4:
                                return 2;
	count=0
	for j in range(0,4):
		if list[j][j]=="O" or list[j][j]=="T":
			count=count+1;
		if count==4:
			return 2;
	
	if ( (list[0][3]=="X" or list[0][3]=="T") and (list[1][2]=="X" or list[1][2]=="T") and (list[2][1]=="X" or list[2][1]=="T") and (list[3][0]=="X" or list[3][0]=="T")):
		return 1;
	if ((list[0][3]=="O" or list[0][3]=="T") and (list[1][2]=="O" or list[1][2]=="T") and (list[2][1]=="O" or list[2][1]=="T") and (list[3][0]=="O" or list[3][0]=="T")):
                return 2;
	for i in range(0,4):
		for j in range(0,4):
			if list[i][j]==".":
				return 3;
	return 4;
for i in range(0,x):
	list1=[]
	if i!=0:
                line=raw_input()
	for j in range(0,4):
		line=raw_input()
		list1.append(line)
	answer=check(list1)
	str1="Case #"
	str1=str1+str(i+1)
	str1=str1+":"
	if answer==1:
		print str1,"X won"
	if answer==2:
		print str1,"O won"
	if answer==3:
		print str1,"Game has not completed"
	if answer==4:
		print str1,"Draw"
	
