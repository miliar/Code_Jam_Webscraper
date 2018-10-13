text=[]
answer=[]
f=open("jam-2.in", "r")
text=f.readlines()
ans=[]

m=0
for x in text[1:]:
	answer.append(0)
	items=map(int, x.split())
	for y in sorted(items[3:]):
		if y>=items[2]:
			for t in range(11):
				t=int(t)
				y=int(y)
				if int(items[1])>0:
					temp_1=[t, t, t-2]
					temp_2=[t+2, t+2, t]
					temp_3=[t, t-1, t-2]
					temp_4=[t, t-2, t-2]
					temp_5=[t, t+1, t+2]
					if sum(temp_1)==y and max(temp_1)>=int(items[2]):
						items[1]=int(items[1])-1
						answer[m]+=1
						break
					if sum(temp_2)==y and max(temp_2)>=int(items[2]):
						items[1]=int(items[1])-1
						answer[m]+=1
						break
					if sum(temp_3)==y and max(temp_3)>=int(items[2]):
						items[1]=int(items[1])-1
						answer[m]+=1
						break
					if sum(temp_4)==y and max(temp_4)>=int(items[2]):
						items[1]=int(items[1])-1
						answer[m]+=1
						break
					if sum(temp_5)==y and max(temp_5)>=int(items[2]):
						items[1]=int(items[1])-1
						answer[m]+=1
						break
				if int(items[1])==0:
					temp_1=[t, t, t-1]
					temp_2=[t, t, t]
					temp_3=[t, t, t+1]
					if sum(temp_1)==y and max(temp_1)>=int(items[2]):
						answer[m]+=1
						break
					if sum(temp_2)==y and max(temp_2)>=int(items[2]):
						answer[m]+=1
						break
					if sum(temp_3)==y and max(temp_3)>=int(items[2]):
						answer[m]+=1
						break

	m+=1






num=1
for x in answer:
	ans.append("Case #%s: %s \n" % (num, x))
	num+=1
f.close()
f=open("ans.txt", "w")
f.writelines(ans)
f.close()
