# Leon Xueliang Liu 2017

from math import floor, ceil, log, pow

with open('C-small-2-attempt0.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # # of cases
data = [[val for val in line.split()] for line in content[1:]]

result = [] # list of results

for n in range(T):
	N = int(data[n][0])
	K = int(data[n][1])
	
	s = pow(2, floor(log(K, 2)))
	mt = N-s+1

	a = floor(mt/s)
	b = ceil(mt/s)

	if N-s*a >= K:
		x = ceil((b-1)/2)
		y = floor((b-1)/2)
	else:
		x = ceil((a-1)/2)
		y = floor((a-1)/2)

	result.append([int(x), int(y)])



#write to output
with open('C-small-2-attempt0.txt','w+') as f:
	for count, entry in enumerate(result):
		f.write("Case #{}: {} {}\n".format(count+1, entry[0], entry[1]))
		print("Case #{}: {} {}\n".format(count+1, entry[0], entry[1]))

