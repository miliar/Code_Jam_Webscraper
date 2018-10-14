def main():
	[N,R,O,Y,G,B,V] = map(int,raw_input().split())
	if (R - Y - B) > 0 or (Y - R - B) > 0 or (B - Y - R) > 0:
		return "IMPOSSIBLE"
	s = str("D")
	var = True
	i = 0
	temp = [[R,"R"],[Y,"Y"],[B,"B"]]
	while i < N:
		temp.sort()
		i+=1
		temp.sort()
		if var:
			start = temp[-1][1]
			var = False
		if temp[-1][1] != start and temp[1][0] == temp[-1][0] and temp[1][1] != s[-1]:
			if temp[1][1] == start:
				temp[1][0] -=1
				s+=temp[1][1]
				continue
		if temp[-1][1] != s[-1]:
			temp[-1][0] -= 1
			s+= temp[-1][1]
		else:
			temp[1][0] -= 1
			s+=temp[1][1]
	return s[1:]
	
T = input()
for i in range(T):
	res = main()
	print "Case #" + str(i+1) + ":",res
