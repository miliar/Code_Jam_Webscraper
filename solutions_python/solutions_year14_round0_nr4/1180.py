f=file("D-large.in")
op=file("Dlarge.op","w")
total_line=f.readline()
total_line=int(total_line)

def war(naomi,ken):

	if naomi[-1]<ken[0]:
		return 0	
	while len(naomi)!=0:
		naomi_block=naomi[0]
		for	i in range(len(ken)):
			ken_block=ken[i]
			if ken_block >naomi_block:
				naomi.remove(naomi_block)
				ken.remove(ken_block)
				break
			
		if len(naomi)!=0 and naomi[0]>ken[-1]:
			break
		
	return len(naomi) 
	
	
		
def deceit(naomi,ken):
	
	#print naomi
	#print ken
	
	won=0
	while len(naomi)!=0:
		if naomi[0]>ken[-1]:
			return won+len(naomi)
		if naomi[-1]<ken[0]:
			return won
	
		if naomi[0]>ken[0]:
			naomi.remove(naomi[0])
			ken.remove(ken[0])
			won+=1
		else:
			naomi.remove(naomi[0])
			ken.remove(ken[-1])
	
for i in range(total_line):
	
	total_items=int(f.readline())
	
	line=f.readline().split('\n')[0]
	list1=line.split(' ')
	naomi_list=[float(data) for data in list1]

	line=f.readline().split('\n')[0]
	list2=line.split(' ')
	ken_list=[float(data) for data in list2]
	
	naomi_sorted=naomi_list
	naomi_sorted.sort()
	ken_sorted=ken_list
	ken_sorted.sort()
	
	
	war_won_cnt=war(naomi_sorted,ken_sorted)
	#print war_won_cnt
	naomi_list=[float(data) for data in list1]
	ken_list=[float(data) for data in list2]
	naomi_sorted=naomi_list
	naomi_sorted.sort()
	ken_sorted=ken_list
	ken_sorted.sort()
	
	deceit_won_cnt=deceit(naomi_sorted,ken_sorted)
	#print deceit_won_cnt
	
	string = "case #"+str(i+1)+": "
	string =string +str(deceit_won_cnt)+" "+ str(war_won_cnt)
	op.write(string+"\n")

	print string	
