#!/usr/bin/env python2.7


import sys
import math


MAX_M = 200
CASE_NUM = 0

def read_data(filename = ''):
	global CASE_NUM

	input_f = sys.stdin
	if filename != '':
		input_f = open(filename,'r')

	#data which used by handle_data()
	input_fun1_l = []
	
	CASE_NUM = int(input_f.readline())
	
	#case init data
	for case in range(0,CASE_NUM):
		#case data sets init
		# data_count = int(input_f.readline())
		list_of_input = []
		#case depends

		line = input_f.readline()
		parts = line.strip().split()
		list_of_input= map(float,parts)
		
		

		#for every case if there are few datas
		
		#add to result set
		input_fun1_l.append(list_of_input)

	input_f.close()
	return input_fun1_l


def write_data(result_l,filename = ''):
	global CASE_NUM
	output_f = sys.stdout
	if filename != '':
		output_f = open(filename,'w')
	for i in range(0,CASE_NUM):
		output_f.write(('Case #%d: ' % (i+1) )+ str(result_l[i])+ '\n')
	
	output_f.close()
	return


def handle_data(matrix_arr):
	result_l = []
	for matrix in matrix_arr:
		result_l.append(caculate_time(matrix))
	return result_l


def should_buy_future(c, f, inc_f,x):
	instant_time = (x - c)/ f
	f2 = f + inc_f
	future_time = x / f2

	if instant_time < future_time:
		return False
	else:
		return True

def caculate_time(input_l):
	now_c = input_l[0]
	inc_f = input_l[1]
	now_f = 2.0
	x = input_l[2]
	time = 0
	while should_buy_future(now_c, now_f, inc_f, x):
		farm_time = now_c / now_f
		time += farm_time
		now_f += inc_f
	time += (x) / now_f

	return ("{:.7f}").format(time)




if __name__ == '__main__':
	matrix_arr = read_data('B-large.in')
	result_l = handle_data(matrix_arr)
	write_data(result_l,'B-large.out')