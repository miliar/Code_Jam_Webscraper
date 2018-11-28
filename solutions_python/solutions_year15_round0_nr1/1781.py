
case_num = int(input())

for case in range(case_num):
	data = input()
	args = data.split(" ")
	s_max = int(args[0])

	au_list = [0] * (s_max + 1)
	aup = args[1] 
	num_hman = 0;
	for index in range(len(au_list)):
		au_list[index] = int(aup[index])
	dp = [0] * (s_max + 1)
	for index in range(1, len(au_list)):
		dp[index] = dp[index-1] + au_list[index-1]
		if au_list[index] != 0 and dp[index] < index:
			num_hman += index - dp[index]
			dp[index] = index
	print("Case #", case+1, ": ", num_hman, sep='')
