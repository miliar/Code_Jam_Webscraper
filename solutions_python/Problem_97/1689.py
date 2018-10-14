
def main():
	finput = open("C-small-attempt0.in", 'r')
	foutput = open("output.txt", 'w')
	
	T = int(finput.readline())
	for case in range(T):
		A, B = map(int, finput.readline().rstrip('\n').split(' '))
		count = 0
		for number in range(A, B):
			nb_str = list(str(number))
			tmp_nb_str = ['']*len(nb_str)
			dup_str = []
			for j in range(1, len(nb_str)):
				for i in range(0, len(nb_str)):
					tmp_nb_str[(i+j)%len(nb_str)] = nb_str[i]
				dup_str.append(int(''.join(tmp_nb_str)))
				if (len(dup_str)!=len(set(dup_str))):	
					continue
				
				if int(''.join(tmp_nb_str)) > int(''.join(nb_str)) and int(''.join(tmp_nb_str)) <= B:
				  	count += 1
				
		foutput.write('Case #' + str(case+1) + ': ' + str(count) + '\n')
	
	foutput.close()
	finput.close()		

if '__main__' == __name__ :
	main()
