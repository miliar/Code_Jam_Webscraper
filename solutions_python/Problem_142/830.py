

def solve_problem(strings,N):
	reps= {}
	i= 0
	n= len(strings[0])
	j= 0
	while i<n:
		c= strings[0][i]
		while i<n and c==strings[0][i]:
			i+= 1
		reps[(c,j)]= []
		j+= 1
	for string in strings:
		i= 0
		n= len(string)
		k= 0
		while i<n:
			c= string[i]
			if not reps.has_key((c,k)):
				return 'Fegla Won'
			j= 0
			while i<n and c==string[i]:
				i+= 1
				j+= 1
			reps[(c,k)].append(j)
			k+= 1
	n_moves= 0 
	for c in reps:
		if len(reps[c])<N:
			return 'Fegla Won'
		avg= 0.0
		for i in range(N):
			avg+= reps[c][i]
		avg= int(round(avg/N))
		std_dev= 0
		for i in range(N):
			std_dev+= abs(reps[c][i]-avg)
		n_moves+= std_dev
	return n_moves

file= open('the_repeater.in')
input= file.read().split('\n')
file.close()

T= int(input[0])
i= 0
j= 1
while i < T:
	N= int(input[j])
	strings= []
	for k in range(1,N+1):
		strings.append(input[j+k])
	print 'Case #' + str(i+1)	+ ': ' + str(solve_problem(strings,N))
	j+= N+1
	i+= 1
