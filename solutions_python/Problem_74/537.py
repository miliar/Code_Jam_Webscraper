#!/usr/bin/env python

N = input()


a_time = 1
state = {
	'O' : { 'clk' : 1, 'btn' : 1 },
	'B' : { 'clk' : 1, 'btn' : 1 }
}

def make_move(who, btn):
	global a_time, state
	move_end_time = state[who]['clk'] + abs(btn-state[who]['btn'])
	next_time = max(move_end_time, a_time)
	a_time = next_time + 1 # must also press the button
	state[who]['clk'] = a_time
	state[who]['btn'] = btn

for n in range(N):

	a_time = 1
	state = {
		'O' : { 'clk' : 1, 'btn' : 1 },
		'B' : { 'clk' : 1, 'btn' : 1 }
	}


	line = raw_input()
	flds = line.strip().split(" ")[1:]
#	print flds
	for i in range(0, len(flds), 2):
		make_move(flds[i], int(flds[i+1]))
#		print flds[i], flds[i+1]
	print "Case #%d: %d"%(n+1,a_time-1)
