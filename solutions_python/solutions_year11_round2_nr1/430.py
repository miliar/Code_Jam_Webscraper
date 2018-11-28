# Google Code Jam 2011  
# Javier Fernandez 

# played dictionary: {'A':{'A':'.', 'B':'1' ...} ...}
from __future__ import division
import sys

def rpi(wp,owp,oowp):
	return (0.25*wp + (0.50*owp)+(0.25*oowp))

def get_points(character):
	if (character=='1'):
		return 1
	elif (character=='0'):
		return 0

def calc_wp(played,team,throw):
	team_games = played[team]
	acum = 0
	size = 0
	for	opp in team_games:
		if (team_games[opp]=='.'):
			continue
		if (opp == throw):
			continue
		acum+=get_points(team_games[opp])
		size+=1
		
	return acum/size
	
def calc_owp(played,team):
	acum=0
	size=0
	for t in played:
		#not count me in average
		if (t==team):
			continue
		if (played[team][t]=='.'):
			continue
		# throw away me
		acum+=calc_wp(played,t,team)
		size+=1
	return acum/size
	
def calc_all_owp(played):
	all_owp ={}
	for team in played:
		all_owp[team] = calc_owp(played,team)
	return all_owp
	
def avg_owp(all_owp,played,team):
	acum=0
	size=0
	for t in all_owp:
		if(t==team):
			continue
		if(played[team][t]=='.'):
			continue
		acum+=all_owp[t]
		size+=1
	return acum/size
		
#calculate rpi for every team
def ncca_rpi(played,num_teams,out):		
	all_owp = calc_all_owp(played)
	for count in range(num_teams):
		team = str(count+1)
		wp = calc_wp(played,team,'none')
		owp = all_owp[team]
		oowp = avg_owp(all_owp,played,team)
		out.write(str(rpi(wp,owp,oowp))+'\n')
		
def get_played(num_teams,in_file):
	played={}
	for n in range(num_teams):
		played[str(n+1)]={}
	for team in range(num_teams):
		rivals = in_file.readline().strip('\n')
		count = 1
		for r in rivals:
			played[str(team+1)][str(count)]=r
			count+=1
	return played

def solution(in_file,out_file):
	num_cases = int(in_file.readline())
	for c in range(num_cases):
		out_file.write("Case #"+str(c+1)+":"+'\n')
		num_teams = int(in_file.readline())
		played = get_played(num_teams, in_file)
		ncca_rpi(played,num_teams, out_file)
	
out_file = open('output.out','w+')
in_file = sys.stdin
solution(in_file,out_file)

		
		
		
		
		
		