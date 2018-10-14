t = input()
for case in range(1,t+1):
	s = raw_input()
	a = [int(x) for x in s]
	ans = ["0"]
	flag = False
	dissolve = False
	for i in range(len(a)-1):
		if flag:
			ans.append("9")
			continue
		if a[i] > a[i+1]:
			# print ans[bf_ctr],a[i]
			if a[i] == 1:
				dissolve = True
			if ans[-1] == str(a[i]):
				ans[-1] = str(a[i]-1)
				ans.append("9")
			else:
				ans.append(str(a[i]-1))
			flag = True
		else:
			ans.append(str(a[i]))
	if dissolve:
		ans = ["9" for i in range(len(a)-1)]
	elif flag:
		ans.append("9")
	else:
		ans.append(str(a[-1]))
	print "Case #%d: %d" % (case,int("".join(ans)))