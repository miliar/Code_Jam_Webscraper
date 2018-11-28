# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="assim"
__date__ ="$Sep 3, 2009 3:31:06 PM$"


def is_exist(word_list, case):
	def is_in_case_list(w, c):
		#print "w: ", w, "c: ",  c
		for i in range(len(w)):
			if w[i] not in c[i]:
				break
		else:
			return True

		return False

	#word_list = word.split()
	case_list = []
	temp = ""
	in_br = False
	for i in case:
		if i == '(':
			in_br = True
			temp = ""
			continue
		elif i == ')':
			in_br = False
			case_list.append(temp)
			continue
		if in_br:
			temp = temp + str(i)
		else:
			case_list.append(i)
	count = 0
	for w in word_list:
		if is_in_case_list(w,case_list):
			count +=1
	return count


def q1():
	infile = open('infine','r')
	# @type infile file
	first_line = infile.readline()
	w = first_line.split()
	w_len = int(w[0])
	strs = int(w[1])
	cases = int(w[2])

	w_list = []

	for i in range(strs):
		w_list.append(infile.readline()[:-1])

	c_list = []
	for i in range(cases):
		c_list.append(infile.readline()[:-1])
	i = 1
	#print w_list
	#print c_list

	ofile = open('ofile', 'w')
	# @type ofile file

	for c in c_list:
		ofile.writelines("Case #%s: %s\n" %( str(i), str(is_exist(w_list, c))))
		i += 1
	infile.close()
	ofile.close()


def q2():

	infile = open('b-l-i','r')
	outfile = open('b-l-o', 'w')

	def go_where(m,i,j):
		#N W E S
		t = m[i][j]
		m_i = len(m)
		m_j = len(m[i])
		#l = [ (i-1, j),	(i, j-1),(i, j+1),(i+1, j)]
		#N
		ret = (i, j)
		if i != 0:
			n = m[i-1] [j]
			if n < t:
				ret = (i-1, j)
				t  = n
		if j != 0:
			n = m[i] [j-1]
			if n < t:
				ret = (i, j-1)
				t  = n
		if j!= m_j-1:
			n = m[i] [j+1]
			if n < t:
				ret = (i, j+1)
				t  = n
		if i!= m_i-1:
			n = m[i+1] [j]
			if n < t:
				ret = (i+1, j)
				t  = n
		
		if ret == (i,j):
			return False
		return ret

	def solve_map(m_size, m):
		h = m_size[0]
		w = m_size[1]
		sink_list = []
		global c_i
		c_i =  97
		#chr(97) = 'a'
		for i in range(h):
			r = []
			for j in range(w):
				r.append('.')
			sink_list.append(r)
		

		def get_char(mp,x,y):
			global c_i
			if sink_list[x][y] != '.':
				return sink_list[x][y]
			else:
				n = go_where(mp, x, y)
				if n:
					ch = get_char(mp,n[0],n[1])
					#print n, ch
				else:
					ch = chr(c_i)
					c_i = c_i + 1
				sink_list[x][y] = ch
				return ch

		for i in range(h):
			for j in range(w):
				sink_list[i][j] = get_char(m,i,j)
					
		return sink_list


	test_cases = int(infile.readline()[:-1])
	map_size_list = []
	map_list = []


	for i in range(test_cases):
		s = infile.readline()[:-1].split()
		h = int(s[0])
		w = int(s[1])
		map_size_list.append((h, w))
		map  =[]
		for j in range(h):
			r = infile.readline()[:-1].split()
			for k in range(w):
				r[k] = int(r[k])
			map.append(r)
		map_list.append(map)
		output = ""
	for i in range(test_cases):
		# @type outfile file
		outfile.write("Case #%s:\n" %( str(i+1)))
		for r in solve_map(map_size_list[i], map_list[i]):
			st = ""
			for c in r:
				st = st + " " + str(c)
			outfile.write("%s\n" %(st))
	infile.close()
	outfile.close()




		



if __name__ == "__main__":
	n = q2()