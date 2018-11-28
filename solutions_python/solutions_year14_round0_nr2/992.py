#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	C_F_X_list=raw_input().strip().split()
	C=float(C_F_X_list[0])# a farm cost
	F=float(C_F_X_list[1])# farm production
	X=float(C_F_X_list[2])# objective
	
	current_rate=2.0
	accumulated_time=0.0
	
	time_with_current_rate=X/current_rate
	time_to_new_farm=C/current_rate
	time_with_new_farm=time_to_new_farm+X/(current_rate+F)
	
	while (time_with_current_rate> time_with_new_farm):
		accumulated_time+=time_to_new_farm
		current_rate+=F
		
		time_with_current_rate=X/current_rate
		time_to_new_farm=C/current_rate
		time_with_new_farm=time_to_new_farm+X/(current_rate+F)
	
	needed_time=accumulated_time+time_with_current_rate

	print "Case #{}: {}".format(test,needed_time)