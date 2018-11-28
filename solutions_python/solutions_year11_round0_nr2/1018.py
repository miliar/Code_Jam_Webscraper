import sys

def find_list(cases):

	form=int (cases[0])
	print form
	list_form=[]
	cnt=0
	while(cnt<form):
		list_form.append(cases[cnt+1][0])
		list_form.append(cases[cnt+1][1])
		list_form.append(cases[cnt+1][2])
		print list_form
		cnt+=1

	oppose=int (cases[form+1])
	print "oppose=",oppose
	list_oppose=[]
	cnt=0
	while(cnt<oppose):
		list_oppose.append(cases[cnt+1+form+1][0])
		list_oppose.append(cases[cnt+1+form+1][1])
		print"oppose list",list_oppose
		cnt+=1

	items=int (cases[form+1+oppose+1])
	print "items=",items
	list_items=[]
	cnt=0
	while(cnt<items):
		list_items.append(cases[oppose+2+form+1][cnt])
		cnt+=1
	print "items",list_items
	list_result=[]
	for item in list_items:
		list_result.append(item)
		l=len(list_result)
		break_flag=1
		### form
		if l>1:
			cnt=0
			while(cnt<len(list_form)):
				while break_flag==1:
					if len(list_result)>1:
						if((list_result[-1]==list_form[cnt] and list_result[-2]==list_form[cnt+1]) or (list_result[-1]==list_form[cnt+1] and list_result[-2]==list_form[cnt] )):
							list_result.pop()
							list_result.pop()
							list_result.append(list_form[cnt+2])
						else:
							break_flag=-1
					else:
						break_flag=-1
				cnt=cnt+3

		print "adding", list_result
		##oppose
		l2=len(list_result)
		cnt=0
		first_flag=0
		second_flag=0
		
		while (cnt<l2):
			idx=0
			first=0
			second=0				
			while(idx<len(list_oppose)):
				if (list_oppose[idx]==list_result[cnt]):
					first_flag=1
					prev_first_idx=idx
				if (list_oppose[idx+1]==list_result[cnt]):
					second_flag=1
					prev_second_idx=idx
				if(first_flag==1):
					if (list_oppose[prev_first_idx+1]==list_result[cnt]):
						first_flag=2
				if(second_flag==1):
					if (list_oppose[prev_second_idx]==list_result[cnt]):
						second_flag=2				
					
				idx+=2
			cnt+=1
		if(first_flag==2 or second_flag==2):
			list_result=[]
			print "deleting", list_result	
								
	return list_result
	#sys.exit(0)

def main():
	print "hello"
	filename=sys.argv[1]
	fin=open(filename,"r")
	o=open("out.txt","w")
	k=0;
	for line in fin:
		if(k>0):
			cases=line.split()
			print cases
			
			lo=find_list(cases)
			str1='['
			l3=len(lo)
			cnt=0
			for item in lo:
				s=str(item[0])
				if cnt<l3-1:
					str1+=s+","+" "
				else: 
					str1+=s
				cnt+=1
			print>>o,"Case #"+str(k)+": "+str1+']'
			
		k+=1

if __name__=="__main__":
	main()
