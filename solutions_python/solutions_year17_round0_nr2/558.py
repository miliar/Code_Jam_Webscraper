def tidy_num(N):
	flag = True
	s_form = list(str(N))
	idx = -1
	for i in range(len(s_form)-1):
		if s_form[i] > s_form[i+1]:
			flag = False
			idx = i+0
			break
	if flag:
		return N
	else:
		s_form[idx] = str(int(s_form[idx])-1)
		for i in range(idx+1,len(s_form)):
			s_form[i] = '9'
		#print('s_form:',s_form)
		return tidy_num(int(''.join(s_form)))
			
T=int(input())
for i in range(T):
	N = int(input())
	print(tidy_num(N))
