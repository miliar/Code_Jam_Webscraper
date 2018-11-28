case_nr = int(input())

for i in range(case_nr):
	text, number = input().split()
	txt = list(text)
	nr = int(number)
	cnt = 0
	if "-" in txt:
		for idx in range(len(txt[:len(txt)-nr+1])):
			if txt[idx] == "-":
				for x in range(nr):
					if txt[idx+x]=="-":
						txt[idx+x]="+"
					else:
						txt[idx+x] = "-"
				cnt += 1
	if "-" not in txt:
		print("Case #{}: {}".format(i+1,cnt))
	else:
		print("Case #{}: IMPOSSIBLE".format(i+1))
