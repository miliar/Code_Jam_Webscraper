for l in range(int(input())):
	m = str(input())
	if int(m) == int("".join(sorted(m))):
		answer = int(m)
	else:
		while(int("".join(m)) != int("".join(sorted(m)))):
			m = list(m)
			t = m.index(sorted(m)[-1])
			m[t] = str(int(m[t])-1)
			m[t+1:len(m)] = ["9" for p in range(len(m)-t-1)]
		answer = int("".join(m))


	print("Case #{}: {}".format(l+1,answer))