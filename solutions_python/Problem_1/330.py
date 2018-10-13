class SearchOptimization():
	def search(self,filename,w_file):
		f = open(filename,'r')
		cases = int(f.readline())
		o = open(w_file,'w')
		for c in range(cases):
			e_list = []
			engines = int(f.readline())
			for e in range(engines):
				e_list.append(f.readline())
			
			queries = int(f.readline())
			switch = 0;
			if(queries > 0):
				query = f.readline()
			s_list = e_list + []
			i = 0
			while(i < queries):
				if(query in s_list):
					t_list = []
					for s in s_list:
						if(s != query):
							t_list.append(s)
					if(len(t_list) == 0):
						s_list = e_list + []
						switch = switch + 1
					else:
						s_list = t_list + []
						i = i + 1
						if(i < queries):
							query = f.readline()
				else:
					i = i + 1
					if(i < queries):
						query = f.readline()
			else:
				o.write('Case #' + str(c+1) + ':  ' + str(switch) + '\n')
				print switch
		else:
			o.close()