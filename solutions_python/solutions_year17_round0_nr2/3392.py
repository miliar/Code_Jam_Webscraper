def transform_n(decrement_char,l_n):
	if l_n[decrement_char]!='0':
		l_n[decrement_char]=str(int(l_n[decrement_char])-1)
		for i in range(decrement_char+1, len(l_n)):
			l_n[i]='9'
	return l_n

n_cases=input()
for i in range(int(n_cases)):
	n=input()
	list_n=[l for l in n]
	final_n=-1
	if list_n==sorted(list_n):
		final_n=int(''.join(list_n))
	else:
		for j in range(len(list_n)):
			l=transform_n(j,list_n[:])
			#print(l)
			if l==sorted(l):
				final_n=int(''.join(l))
	print('Case #%d: %d' % (i+1, final_n))
