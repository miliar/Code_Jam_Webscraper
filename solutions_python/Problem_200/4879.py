i = 0
flg = False
with open("B-small-attempt2.in") as f:
	for line in f:
		if (i == 0): 
			i += 1
			continue
		ans = int(line.rstrip())
		while (True):
			chars = list(str(ans))
			chars_sorted = list(str(ans))
			chars_sorted.sort()
			if "0" in chars or chars != chars_sorted:
				ans -= 1
				flg = True
			else:
				break
		print("Case #"+str(i)+": "+str(ans))
		i += 1