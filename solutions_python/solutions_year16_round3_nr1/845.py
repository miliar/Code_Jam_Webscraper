def solve(n,arr,answer):

	flag = True
	for i in arr:
		if i != 0:
			flag = False
			break
	if flag:
		return answer


	for i in range(-1,len(arr)):

		if i != -1 and temp[i] == 0:
			continue


		for j in range(-1,len(arr)):

			if j != -1 and arr[j] == 0:
				continue

			if i == -1 and j ==-1:
				continue

			flg = True
			temp = arr[:]

			if i != -1:
				temp[i] = temp[i] - 1

			if j != -1:
				temp[j] = temp[j] - 1

			total = 0

			for k in temp:
				total = total + k

			for k in temp:
				if k > total/2:
					flg = False
					break;

			if flg:

				ans1 = ""
				ans2 = ""

				if i != -1:
					ans1 = chr(i+65)
				if j != -1:
					ans2 = chr(j+65)

				ans = ans1+ans2

				answer.append(ans)


				return solve(n,temp,answer[:])



t = int(raw_input())
for i in range(0,t):
	n = int(raw_input())	
	s = (raw_input()).split()
	arr = []
	for ss in s:
		arr.append(int(ss))
	ans =  solve(n,arr,[])
	print "Case #"+str(i+1)+":",
	print ' '.join(ans)
