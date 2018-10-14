#!/usr/bin/python
# -*- coding: utf-8 -*-

problem = 'A'
input_type = 'large'
id_ = '0'

in_file  = open(problem+'-'+input_type+'-'+id_+'.in', 'r')
out_file = open(problem+'-'+input_type+'-'+id_+'.out', 'w')

in_data = [line.rstrip() for line in in_file]
out_data = ''


ncases = int(in_data[0])
for j in range(1,ncases+1):
	s = in_data[j]
	n = int(s.split(' ')[0])
	orders = [[0 if s.split(' ')[2*k-1] == 'O' else 1,int(s.split(' ')[2*k])] for k in range(1,n+1)]
	print n, orders
	r_pos = [1, 1]
	turn = 0
	task = 0
	
	while task < len(orders):
		act = orders[task][0]

		task1 = task+1
		while task1<n and orders[task1][0]==act: task1 += 1
		if task1<n and orders[task1][1]!=r_pos[1-act]:
			r_pos[1-act] = r_pos[1-act]-1 if orders[task1][1] < r_pos[1-act] else r_pos[1-act]+1

		if r_pos[act] == orders[task][1]:
			task = task+1
		else:
			r_pos[act] = r_pos[act]-1 if orders[task][1] < r_pos[act] else r_pos[act] + 1

		turn = turn+1
	out_file.write("Case #" + str(j) + ": " + str(turn) + '\n')

in_file.close()
out_file.close()


