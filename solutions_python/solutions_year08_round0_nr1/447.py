import sys,os
os.chdir(os.getcwdu() + "/Desktop")
f=open("input.txt","r")
f1=open("output.txt","w")
list=f.readline()
for i in range(0,int(list[:-1])):
	search_engine_size=int(f.readline()[:-1])
	search_engines=[]
	for j in range(0,int(search_engine_size)):
		search_engines.append(f.readline()[:-1])
	no_of_queries=int(f.readline()[:-1])
	if no_of_queries==0:
		print no_of_queries
		count=0
		f1.write("Case #" + str(i+1) + ": "+ str(count))
		f1.write("\n")
	else:
		print "else" + str(no_of_queries)
		query_list=[]
		for k in range(0,no_of_queries):
			query_list.append(f.readline()[:-1])
		index=0
		count=-1       
		while not index>=len(query_list):
			print index,len(query_list)
			count+=1
			search_index=[]
			engine=''
			for search_engine in search_engines:
				if search_engine in query_list[index:]:
					search_index.append(query_list[index:].index(search_engine))
				else:
					engine=search_engine
					index=len(query_list)
					break
			if engine=='':
				print search_index
				engine=query_list[index+max(search_index)]
				index=index+max(search_index)
			
		f1.write("Case #" + str(i+1) + ": "+ str(count)) 
		f1.write("\n")
	
f.close()
f1.close()