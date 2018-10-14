def add(x, y): return x+y

def rpi(played, wins):
	teams = len(played)
	wp = [0] * teams
	for i in range(teams):
		tot_wins = reduce(add, wins[i])
		tot_played = reduce(add, played[i])
		wp[i] = float(tot_wins)/tot_played
	wp_owp = [[0] * teams for i in range(teams)]
	for i in range(teams):
		for j, val in enumerate(played[i]):
			if val == 1:
				tot_wins = reduce(add, wins[j][i+1:], reduce(add, wins[j][:i], 0))
				tot_played = reduce(add, played[j]) - 1
				wp_owp[i][j] = float(tot_wins)/float(tot_played)
	owp = [0] * teams
	for i in range(teams):
		owp[i] = float(reduce(add, wp_owp[i]))/reduce(add, played[i])
	
	oowp = [0] * teams
	for i in range(teams):
		sum = 0
		for j, val in enumerate(played[i]):
			if val == 1:
				sum = sum + owp[j]
		oowp[i] = float(sum)/reduce(add, played[i])
	
	rpi = [0] * teams
	for i in range(teams):
		rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
		
	return rpi
	
def solve():
	fin = open("input.txt")
	lines = fin.readlines()
	line_num = 0

	tot_case = int(lines[line_num])
	line_num = line_num + 1	
	fout = open("out.txt", 'w')
	for case in range(tot_case):
		tot_teams =  int(lines[line_num])
		line_num = line_num + 1	

		played = [[0] * tot_teams for i in range(tot_teams)]
		wins = [[0] * tot_teams for i in range(tot_teams)]
		for team in range(tot_teams):
			for i in range(tot_teams):
				val = lines[line_num][i]
				if(val == '1'):
					played[team][i] = 1
					wins[team][i] = 1
				elif(val == '0'):
					played[team][i] = 1
			line_num = line_num + 1	
		
		fout.write("Case #"+str(case+1)+":\n")
		for r in rpi(played, wins):
			fout.write(str(r)+"\n")
			
solve();