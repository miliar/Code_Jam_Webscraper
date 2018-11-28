# Google Code Jam 2011 Qualification Round
# Javier Fernandez (javierfdr@gmail.com)

#data type
# [robot_pos, must_press]

import collections

def bot_sequence(actions):
	# deque collections (reverse order)
	[blue_actions, orange_actions] = split_actions(actions)
	
	blue_bot = [1, False]
	orange_bot = [1, False]
	sec = 0
	action_index = 0
	num_actions = len(actions)
	
	while (action_index < num_actions):
		a = actions[action_index]
		sec+=1
		set_leader(a,blue_bot,orange_bot)

		# last element always cause the list is reversed
		if (len(blue_actions) >0 ): #len is O(1)
			did_blue_press = best_bot_move(blue_bot,int(blue_actions[-1]))
		else:
			did_blue_press = False
		if (len(orange_actions) >0 ):
			did_orange_press = best_bot_move(orange_bot,int(orange_actions[-1]))
		else:
			did_orange_press = False
		
		if (did_blue_press):
			blue_actions.pop()
			action_index+=1

		elif (did_orange_press):
			orange_actions.pop()
			action_index+=1
		
	return sec

# determine de best move towards the current goal
def best_bot_move(bot,action_pos):
	(botpos,must_press) = bot
	if (botpos < action_pos):
		bot[0]+=1
	elif (botpos > action_pos):
		bot[0]-=1
	elif (botpos == action_pos):
		if must_press:
			# press then button
			return True
	# didn't press the button
	return False

# returns blue actions and orange actions in reversed order
def split_actions(actions):
	blue_actions = collections.deque()
	orange_actions = collections.deque()
	for a in actions:
		if a[0]=='O':
			orange_actions.appendleft(a[1:])
		else:
			blue_actions.appendleft(a[1:])	
	return (blue_actions,orange_actions)
	
# defines who is next to press
def set_leader(a,blue_bot,orange_bot):
	if a[0] == 'O':
		blue_bot[1] = False
		orange_bot[1] = True
	else:
		blue_bot[1] = True
		orange_bot[1] = False
	
def parse_file(in_file,out_file):
	num_cases = int(in_file.readline())
	for c in range(num_cases):
		case_data = in_file.readline().split()
		actions = []
		for index in range(1,len(case_data)-1, 2):
			actions.append(case_data[index]+case_data[index+1])
		
		result = bot_sequence(actions)
		out_file.write('Case #'+str(c+1)+': '+str(result)+"\n")
		
		
import sys
in_file = sys.stdin
out_file = open('output.out','w+')
parse_file(in_file,out_file)
	
		