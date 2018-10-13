# Leon Xueliang Liu 2017

with open('B-large.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # # of cases
data = [line.split()[0] for line in content[1:]]

result = [] # list of results

for n in range(T):
	ans = []
	N = str(data[n])
	for char in N:
		ans.append(char)
	L = len(ans)

	# forward pass, if next # is smaller, decrement current, set all later to 9
	for i in range(L-1):
		if int(ans[i]) > int(ans[i+1]):
			ans[i] = str(int(ans[i])-1)
			for j in range(i+1, L):
				ans[j] = '9'
			break

	# reverse pass, if next # is bigger, decrement next, set current to 9
	for i in range(L-1):
		m = int(ans[L-1-i])
		n = int(ans[L-2-i])
		if m < n:
			ans[L-1-i] = '9'
			ans[L-2-i] = str(n-1)

	ans = int("".join(ans))
	result.append(ans)		

#write to output
with open('B-large.txt','w+') as f:
	for count, ans in enumerate(result):
		f.write("Case #{}: {}\n".format(count+1, ans))

