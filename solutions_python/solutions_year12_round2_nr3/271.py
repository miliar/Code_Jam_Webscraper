import sys;

def getList(d,s2) :
	ret_list = []
	l = d[s2]
	ret_list.append(l[1]);
	while not(l[0]==0) :
		s2 = l[0]
		l = d[s2]
		ret_list.append(l[1])

	return ret_list

def defragment(s1,s2) :
	i=0
	s = []
	s1.sort()
	s2.sort()
	for i in range(len(s1)) :
		if s1[i] in s2 :
			s2.remove(s1[i])
		else :
			s.append(s1[i])
	return (s,s2)
	
def print_subset(l) :
	d = {}
	for  i in range(len(l)) :
		temp = []
		if d.has_key(l[i]) :
			print l[i]
			s2 = getList(d,l[i])
			for k in range(len(s2)) :
				sys.stdout.write(str(s2[k])+" ");
			sys.stdout.write("\n");
			return 
		else :
			for key in d.keys() :
				if d.has_key(key+l[i]) :
					s1 = getList(d,key+l[i])
					s2 = getList(d,key)
					s2.append(l[i])
					(s1,s2) = defragment(s1,s2)
					for k in range(len(s1)) :
						sys.stdout.write(str(s1[k])+" ");
					sys.stdout.write("\n");
					for k in range(len(s2)) :
						sys.stdout.write(str(s2[k])+" ");
					sys.stdout.write("\n");
					return 
				else :
					d[key+l[i]]=[key,l[i]]
			d[l[i]]=[0,l[i]]

	sys.stdout.write("Impossible\n")

if __name__=="__main__" :
	t = int(raw_input())

	for  case in range(t) :
		l = str(raw_input()).split(' ')
		l=[int(l[i]) for i in range(1,len(l))]
		sys.stdout.write("Case #"+str(case+1)+":\n");
		print_subset(l)
