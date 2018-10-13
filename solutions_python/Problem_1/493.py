
def maxi_of_list(list):
	if len(list) == 0:
		return 0;
	maxi = list[0];
	for i in range(1,len(list)):
		if list[i] > maxi:
			maxi = list[i];
	return maxi;

def index_in_list(elt,list):
	for i in range(0,len(list)):
		if list[i] == elt:
			return i
	return "false";
	
def get_nb_switch(list_engine, list_query):
	k = 0;
	nb = 0;
	print "   list_engine ",list_engine;
	print list_query,len(list_query);
	while k < len(list_query)-1:
		array = [];
		for i in range(0,len(list_engine)):
			idx = index_in_list(list_engine[i],list_query[k:len(list_query)]);
			if str(idx) != "false":
				array.append(idx);
		print array;
		if len(array) < len(list_engine): 
			return nb;
		max = maxi_of_list(array);
		k = k + max;
		if k < len(list_query):
			nb = nb +1;
	return nb;


#beginnning of main

file_read = open('A-large.in','r')
file_write = open('A-large.ou','w')

lines = file_read.readlines();

for i in range(0, len(lines)):
	lines[i] = lines[i].rstrip();
#~ print lines;
nb_case = int(lines[0]);
current_index = 1;
for i in range(1,nb_case+1):
	print "------ case "+str(i);
	#nb of engines for this case
	nb_engine = int(lines[current_index]);
	current_index = current_index+1;
	list_engine = lines[current_index:current_index+nb_engine];
	current_index = current_index + nb_engine;
	
	#nb of query for this case
	nb_query = int(lines[current_index]);
	current_index = current_index+1;
	list_query = lines[current_index:current_index+nb_query];
	current_index = current_index + nb_query;
	
	nb = get_nb_switch(list_engine,list_query);
	print "   nb = "+str(nb);
	file_write.write("Case #"+str(i)+": "+str(nb)+"\n");

file_read.close();
file_write.close();

