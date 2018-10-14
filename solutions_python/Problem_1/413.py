import sys
from sets import Set

def main():
	file = sys.argv[1]
	fin = open(file, "r")
	fout = open("output.txt", "w")
	num_inputs = int(fin.readline())
	print "num_inputs:", num_inputs
	for i in range(num_inputs):
		num_search_engine = int(fin.readline())
		print "num_search_engine:", num_search_engine
		list_search_engines=[]
		for j in range(num_search_engine):
			list_search_engines.append(fin.readline().replace("\n","").replace("\r",""))
		
		print "list_search_engines:", list_search_engines
		set_search_engines = Set(list_search_engines)
		print "set_search_engines:", set_search_engines	
		num_queries = int(fin.readline())	
		query_list = []
		for j in range(num_queries):
			query_list.append(fin.readline().replace("\n","").replace("\r",""))	
		
		query_list.reverse()
		print "query_list:", query_list		
		
		change_needed = 0
		
		temp_set= Set()
		while len(query_list)>0:
			query = query_list.pop()				
			if query in set_search_engines:
				temp_set.add(query)

			if temp_set == set_search_engines:
				change_needed = change_needed +1
				query_list.append(query)
				temp_set.clear()

		print "change needed:", change_needed
		fout.write("Case #"+str(i+1)+": "+str(change_needed)+"\n")

if __name__ == "__main__":
    main()
