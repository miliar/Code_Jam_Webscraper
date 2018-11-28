file=open('B-large.in','r')
text=file.read()
text=text.split('\n')
a=1
answer=[]
subtract=[]
while a<=100:
	answer2=[]
	subtract=[]
	file=text[a].split(' ')
	length=len(file)
	surprising=int((file[1]))
	best=int(file[2])
	b=3
	while b<length:
		num=int(file[b])
		mod=num%3
		if mod==0:
			if num==0:
				max=0
				if max>=best:
					answer2.append(max)
				else:
					pass
			else:
				max=num/3
				if max>=best:
					answer2.append(max)
				else:
					max=(num/3)+1
					if max>=best:
						answer2.append(max)
						subtract.append(max)
					else:
						pass
		elif mod==1:
			max=(num+2)/3
			if max>=best:
				answer2.append(max)
			else:
				pass
		elif mod==2:
			max=(num+1)/3
			if max>=best:
				answer2.append(max)
			else:
				max=(num+4)/3
				if max>=best:
					answer2.append(max)
					subtract.append(max)
				else:
					pass
		b=b+1
	answer2=int(len(answer2))
	subtract=int(len(subtract))
	if subtract>=surprising:
		subtraction=subtract-surprising
	else:
		subtraction=0
	ans=answer2-subtraction
	ans="Case #"+`a`+": " + `ans`
	answer.append(ans)
	a=a+1
answer="\n".join(answer)
file2=open('output.txt','w')
file2.writelines(answer)
file2.close()