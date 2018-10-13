def solve(parsed_input):
	D, horses = parsed_input
	max_time = 0
	for horse in horses:
		Ki, Si = horse
		time = (D - Ki) / float(Si)
		if time > max_time:
			max_time = time
	return D / max_time
	

def parse():
	D, N = [int(i) for i in raw_input().split()]
	horses = []
	for n in range(N):
		horses.append((int(i) for i in raw_input().split()))
	return (D, horses)

T = int(raw_input())
for t in range(1, T+1):
	print("Case #{0}: {1}".format(t, solve(parse())))
 
