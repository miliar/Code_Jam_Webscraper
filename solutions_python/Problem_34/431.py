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



if __name__ == "__main__":

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
	for c in c_list:
		print "Case #%s: %s" %( str(i), str(is_exist(w_list, c)))
		i += 1


