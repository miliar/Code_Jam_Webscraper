def solve_case(case):
	case = case.split(' ')
	bots = [[0, 1], [0,1]]
	idle_time = [0, 0]
	tot_buttons = int(case[0])
	for j in range(tot_buttons):
		cur_bot = 0 if case[1+j*2] == 'O' else 1
		button_no =  int(case[2*j + 2])
		time_req = max(1, (abs(button_no - bots[cur_bot][1]) + 1) - idle_time[cur_bot])
		bots[cur_bot][0] += idle_time[cur_bot] + time_req
		bots[cur_bot][1] = button_no
		idle_time[cur_bot] = 0
		idle_time[cur_bot - 1] += time_req
	
	return max(bots[0][0], bots[1][0])

fin = open('input11.txt')
fout = open('out11.txt','w')

inp = fin.readlines()
tot_case = int(inp[0])
for i in range(1, tot_case+1):
	fout.write("Case #" + str(i) + ": " + str(solve_case(inp[i])) + "\n")
	
fin.close()
fout.close()