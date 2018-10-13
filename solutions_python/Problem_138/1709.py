import bisect
with open("input") as f:
	raw_data=f.read().split("\n")
	if raw_data[-1]:
		index=None
	else:
		index=-1
index=1
data=[]

for i in range(2,len(raw_data),3):
	data.append((sorted([float(j) for j in raw_data[i].split(" ")]),\
	sorted([float(j) for j in raw_data[i+1].split(" ")])))

def war(blocks):
	naomi,ken=blocks
	score=0
	for i in naomi:
		index=bisect.bisect_left(ken,i)
		if index==len(ken):
			del ken[0]
			score+=1
		else:
			del ken[index]
	return score
def deceitful_war(blocks):
	naomi,ken=blocks
	score=0
	for i in ken[-1::-1]:
		index=bisect.bisect_left(naomi,i)
		if index==len(naomi):
			del naomi[0]
		else:
			del naomi[index]
			score+=1
	return score
with open("output","w") as f:
	for index,item in enumerate(data):
		item2=[item[0][:],item[1][:]]
		f.write("Case #{}: {} {}\n".format(index+1,deceitful_war(item),war(item2)))
