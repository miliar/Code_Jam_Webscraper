
def flip(string,k,end):
	start = end-k
	# for i,n in enumerate(string):
	for i in range(start+1,end+1):
		n = string[i]
		if i>=start and i<=end and n == '+':
			string[i]='-'
		elif i>=start and i<=end and n == '-':
			string[i]='+'

	return string

def find(string):
	index = 0
	for i,n in enumerate(string):
		if n == '-':
			index = i
	return index

def magic(string,k):
	counter = 0
	while '-' in string:
		index = find(string)
		# print index
		string = flip(string,k,index)
		# print string
		counter += 1
		if index<k and '-' in string:
			return 'IMPOSSIBLE'
			break
	return counter

with open('A-large.in','r') as a:
	data = a.read().split('\n')
b = open('b.txt','w') 

for j in range(int(data.pop(0))):	
	N = data[j]
	n,k = N.split(' ')
	n = list(n)
	k = int(k)
	b.write('Case #%d: %s\n' %(j+1,magic(n,k))) 

