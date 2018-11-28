# Leon Xueliang Liu 2017

with open('B-small-attempt0.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # # of cases
data = [[val for val in line.split()] for line in content[1:]]

result = [] # list of results


for n in range(T):
	N = int(data[n][0])

	dic = {}
	dic['R'] = int(data[n][1])
	dic['O'] = int(data[n][2])
	dic['Y'] = int(data[n][3])
	dic['G'] = int(data[n][4])
	dic['B'] = int(data[n][5])
	dic['V'] = int(data[n][6])
	
	ans = []
	start = max(dic, key=dic.get)
	ans.append(start)
	dic[start] = dic[start] - 1

	for i in range(N-1):
		last = ans[-1]
		if last == 'R':
			newdict = {'Y':dic['Y'], 'B':dic['B'], 'G':dic['G']}
			highest = max(newdict.values())
			if highest < 1:
				ans = 'IMPOSSIBLE'
				break
			toplist = [k for k, v in newdict.items() if v == highest]
			
			if 'G' in toplist:
				top = 'G'
			elif start in toplist:
				top = start
			else:
				top = toplist[0]
			ans.append(top)
			dic[top] = dic[top] - 1


		elif last == 'Y':
			newdict = {'R':dic['R'], 'B':dic['B'], 'V':dic['V']}
			highest = max(newdict.values())
			if highest < 1:
				ans = 'IMPOSSIBLE'
				break
			toplist = [k for k, v in newdict.items() if v == highest]
			
			if 'V' in toplist:
				top = 'V'
			elif start in toplist:
				top = start
			else:
				top = toplist[0]
			ans.append(top)
			dic[top] = dic[top] - 1


		elif last == 'B':
			newdict = {'Y':dic['Y'], 'R':dic['R'], 'O':dic['O']}
			highest = max(newdict.values())
			if highest < 1:
				ans = 'IMPOSSIBLE'
				break
			toplist = [k for k, v in newdict.items() if v == highest]
			
			if 'O' in toplist:
				top = 'O'
			elif start in toplist:
				top = start
			else:
				top = toplist[0]
			ans.append(top)
			dic[top] = dic[top] - 1


		elif last == 'O':
			if dic['B'] < 1:
				ans = 'IMPOSSIBLE'
				break
			ans.append('B')
			dic['B'] = dic['B'] - 1


		elif last == 'G':
			if dic['R'] < 1:
				ans = 'IMPOSSIBLE'
				break
			ans.append('R')
			dic['R'] = dic['R'] - 1


		elif last == 'V':
			if dic['Y'] < 1:
				ans = 'IMPOSSIBLE'
				break
			ans.append('Y')
			dic['Y'] = dic['Y'] - 1

		#print(ans)


	if ans != 'IMPOSSIBLE':
		first = ans[0]
		last = ans[-1]
		if (first=='R' and (last not in ['Y','B','G'])) or (first=='Y' and (last not in ['R','B','V'])) or (first=='B' and (last not in ['Y','R','O'])) or (first == 'O' and (last != 'B')) or (first == 'G' and (last != 'R')) or (first == 'V' and (last != 'Y')):
			ans = 'IMPOSSIBLE'

	if ans != 'IMPOSSIBLE':
		ans = "".join(ans)


	result.append(ans)


#write to output
with open('B-small-attempt0.txt','w+') as f:
	for count, ans in enumerate(result):
		f.write("Case #{}: {}\n".format(count+1, ans))
		
		#for row in ans:
		#	f.write(''.join(row))
		#	f.write("\n")
