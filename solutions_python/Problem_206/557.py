# Leon Xueliang Liu 2017

with open('A-large.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # # of cases
data = [[val for val in line.split()] for line in content[1:]]

result = [] # list of results

m = 0
for n in range(T):
	D = int(data[m][0])
	N = int(data[m][1])

	hours = []

	for i in range(N):
		m = m+1
		k = float(data[m][0])
		s = float(data[m][1])
		time = (D-k)/s
		hours.append(time)

	result.append(D/max(hours))
	m = m+1



#write to output
with open('A-large.txt','w+') as f:
	for count, ans in enumerate(result):
		f.write("Case #{}: {}\n".format(count+1, ans))
		
		#for row in ans:
		#	f.write(''.join(row))
		#	f.write("\n")
