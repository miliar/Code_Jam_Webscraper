import re
# readin input
input = open('input.txt')
fl = input.readline()
[L, D, N] = [int(n) for n in fl.split()]

i = 0
dic = {}
while i < D:
	i = i + 1
	word = input.readline().strip()
	dic[word] = 1

i = 0
cases = []
while i < N:
	i = i + 1
	pattern = input.readline().strip()
	cases.append( pattern.replace('(','[').replace(')',']') )

index = 0
for case in cases:
	index = index + 1
	case_res = 0
	for word in dic.keys():
		if re.match(case, word):
			case_res = case_res + 1
	print("Case #"+str(index)+": "+str(case_res))
