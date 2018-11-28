import re
def decidesink(sinks,row,col,checked):
	i=sinks[row][col][0]
	j=sinks[row][col][1]
	if sinks[i][j]==[i,j]:
		checked[i][j]=1
		return [[i,j],checked]
	else:
		[i,j]=sinks[i][j]
		[sinks[i][j],checked]=decidesink(sinks,i,j,checked)
		return [sinks[i][j],checked]
def reranksink(sinks,H,W,checked):
	for i in range(0,H):
		for j in range(0,W):
			
			if checked[i][j]!=1:
				[sinks[i][j],checked]=decidesink(sinks,i,j,checked)
	return sinks


maps_number=input()
for rando in range(0,maps_number):
	temp=raw_input()
	s=re.split(" ",temp)
	H=int(s[0])
	W=int(s[1])
	map=[]
	sinks=[]
	sinks2=[]
	checked=[]
	for i in range(0,H):
		checked1=[]
		for j in range(0,W):
			checked1.append(0)
		checked.append(checked1)
	for j in range(0,H):
		temp=raw_input()
		s=re.split(" ",temp)
		temp1=[]
		temp2=[]
		for k in range(0,W):
			temp1.append(int(s[k]))
			temp2.append([j,k])
		map.append(temp1)
		sinks.append(temp2)
		sinks2.append(temp2)
	for row_num in range(0,H):
		for col_num in range(0,W):
			if not row_num-1 < 0 and not col_num < 0:
				if map[row_num][col_num]> map[row_num-1][col_num]: 
					if sinks[row_num][col_num]==[row_num,col_num]:
						sinks[row_num][col_num][0]=sinks[row_num-1][col_num][0]
						sinks[row_num][col_num][1]=sinks[row_num-1][col_num][1]
						sinks[row_num][col_num]=sinks[row_num-1][col_num]
						sinks2[row_num][col_num]=[row_num-1,col_num]
					elif map[sinks2[row_num][col_num][0]][sinks2[row_num][col_num][1]]> map[row_num-1][col_num]:
						sinks[row_num][col_num][0]=sinks[row_num-1][col_num][0]
						sinks[row_num][col_num][1]=sinks[row_num-1][col_num][1]
						sinks[row_num][col_num]=sinks[row_num-1][col_num]
						sinks2[row_num][col_num]=[row_num-1,col_num]
			if not row_num < 0 and not col_num-1< 0:
				if map[row_num][col_num]> map[row_num][col_num-1]:
					if sinks[row_num][col_num]==[row_num,col_num]:
						sinks[row_num][col_num][0]=sinks[row_num][col_num-1][0]
						sinks[row_num][col_num][1]=sinks[row_num][col_num-1][1]
						sinks[row_num][col_num]=sinks[row_num][col_num-1]
						sinks2[row_num][col_num]=[row_num,col_num-1]
					elif map[sinks2[row_num][col_num][0]][sinks2[row_num][col_num][1]]> map[row_num][col_num-1]:
						sinks[row_num][col_num][0]=sinks[row_num][col_num-1][0]
						sinks[row_num][col_num][1]=sinks[row_num][col_num-1][1]
						sinks[row_num][col_num]=sinks[row_num][col_num-1]
						sinks2[row_num][col_num]=[row_num,col_num-1]
			if not row_num < 0 and not col_num+1 == W:
				if map[row_num][col_num]> map[row_num][col_num+1]:
					if sinks[row_num][col_num]==[row_num,col_num]:
						sinks[row_num][col_num][0]=sinks[row_num][col_num+1][0]
						sinks[row_num][col_num][1]=sinks[row_num][col_num+1][1]
						sinks[row_num][col_num]=sinks[row_num][col_num+1]
						sinks2[row_num][col_num]=[row_num,col_num+1]
					elif map[sinks2[row_num][col_num][0]][sinks2[row_num][col_num][1]]> map[row_num][col_num+1]:
						sinks[row_num][col_num][0]=sinks[row_num][col_num+1][0]
						sinks[row_num][col_num][1]=sinks[row_num][col_num+1][1]
						sinks[row_num][col_num]=sinks[row_num][col_num+1]
						sinks2[row_num][col_num]=[row_num,col_num+1]
			if not row_num+1 == H and not col_num < 0:
				if map[row_num][col_num]> map[row_num+1][col_num]:
					if sinks[row_num][col_num]==[row_num,col_num]:
						sinks[row_num][col_num][0]=sinks[row_num+1][col_num][0]
						sinks[row_num][col_num][1]=sinks[row_num+1][col_num][1]
						sinks[row_num][col_num]=sinks[row_num+1][col_num]
						sinks2[row_num][col_num]=[row_num+1,col_num]
					elif map[sinks2[row_num][col_num][0]][sinks2[row_num][col_num][1]]> map[row_num+1][col_num]:
						sinks[row_num][col_num][0]=sinks[row_num+1][col_num][0]
						sinks[row_num][col_num][1]=sinks[row_num+1][col_num][1]
						sinks[row_num][col_num]=sinks[row_num+1][col_num]
						sinks2[row_num][col_num]=[row_num+1,col_num]

	sinks=reranksink(sinks,H,W,checked)	
	list_of_sinks=[]
	alphabet_sinks=sinks[:]
	print "Case #"+str(rando)+":"
	for k in range(0,H):
		output_str=""
		for l in range(0,W):
			if sinks[k][l]	not in list_of_sinks:
				list_of_sinks.append(sinks[k][l])
			output_str+=str(chr(ord('a') + list_of_sinks.index(sinks[k][l])))
			if l!=W:
				output_str+=" "
		print output_str	
