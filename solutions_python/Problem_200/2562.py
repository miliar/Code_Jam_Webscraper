def get_tidy(N):
	if int(N) < 10:
		return int(N)

	temp = ''
	left,right = ['','']
	for c in range(len(N)-1):
		if N[c] <= N[c+1]:
			temp += N[c]
		else:
			right = '9'*len(N[c+1:])
			mid = str(int(N[c])-1)
			left = temp+mid
			temp = ''
			break
	if temp == '':
		return int(str(get_tidy(left))+right)
	else:
		return int(temp+N[-1:])

def main():
	in_file = open('input.in','r')
	out_file = open('output.txt', 'w')

	inputs = in_file.readlines()

	T = int(inputs.pop(0).strip())
	for t in range(T):
		N = inputs.pop(0).strip()
		tidyNum = get_tidy(N)
		out_file.write('Case #%d: %s\n' % (t+1, tidyNum))

	in_file.close()
	out_file.close()

if __name__ == '__main__':
	main()