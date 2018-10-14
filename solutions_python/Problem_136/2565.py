for case in range(eval(input())):
	var = input().split(" ")
	c = eval(var[0])
	f = eval(var[1])
	x = eval(var[2])
	cps = 2
	t = 0

	while True:
		t1 = x/cps
		t2 = c/cps+x/(cps+f)
		if t1<t2:
			print("Case #", case+1, ": ", sep="", end="")
			print(t+t1)
			break
		else:
			t+=c/cps
			cps+=f
			
