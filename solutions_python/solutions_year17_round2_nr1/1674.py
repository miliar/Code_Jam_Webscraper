import sys
import math
import heapq
input_file = 'test' + '.in'


def solver(D, K, S):
	need_to = D - K
	hours_to_spend = need_to  / S
	print (hours_to_spend)
	minutes_to_spend = hours_to_spend *  60
	best_approach = minutes_to_spend
	km_best = best_approach / 60
	print (km_best, best_approach, minutes_to_spend)
	print (round(D/ km_best))
	return round(D / km_best, 10)


def fastest (D, K, S):
	need_to = D - K
	hours_to_spend = need_to / S
	minutes_to_spend = hours_to_spend * 60
	
	return minutes_to_spend

def aribter(list, y):

	return_list = []
	for x in list:
		heapq.heappush(return_list, (fastest  (y,  x[0], x[1]), x ))
	return return_list[-1][-1]

def input_parser(input_file):
	with open(input_file) as fin:
		fix = fin.read().split()
		return_list = []
		amount = int(fix[0])
		fix = fix[1:]
		for m in range(amount):
			print (fix)
			x, y = int(fix[0]), int(fix[1])
			del fix[0]
			del fix[0]
			print (fix)
			temp_list = []
			for i in range(y):
				a, b = int(fix[0]), int(fix[1])
				del fix[0]
				del fix[0]
				print (a, b)
				temp_list.append((a,b))
			return_list.append(((x, y), temp_list))
		return return_list 

def final_solver(final_list):
	ultimate_list = []
	for element in final_list:
		x, y = element[0]
		test_case = element[1]
		K, S = aribter(test_case, x)
		ultimate_list.append(solver(x, K, S))
	return ultimate_list


zny = input_parser(input_file)
print (final_solver(zny))
yzn = final_solver(zny)
def outputer(output_file, some_list):
	with open(output_file, 'w') as outf:
		x = 1
		for element in some_list:
			outf.write('Case #%d: %.10f\n' % (x, float(element)))
			x += 1
	print ('DONE')
outputer('lashlo.out',yzn)

print (solver(2525, 2400, 5))
print (solver(300, 120, 60))
print (solver(100, 70, 10))