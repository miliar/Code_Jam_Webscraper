import sys
import re

input_arr = []
c_arr = []
f_arr = []
x_arr = []
ans_arr = []

def read_file():

	with open("jamq2i.txt", 'r') as f:
		count = 0
		for line in f:
			if count != 0:
				# print line[:-1]
				arr = line[:-1].split(" ")
				c_arr.append(float(arr[0]))
				f_arr.append(float(arr[1]))
				x_arr.append(float(arr[2]))


			count+=1
	f.close()

def calc_stuff():
	for x in xrange(len(c_arr)):
		done = False
		income = 2.0
		remainder = x_arr[x]
		elapsed = 0.0
		while not done:
			eta = remainder/income
			farm = (c_arr[x]/income) + remainder/(income+f_arr[x])
			if eta <= farm:
				done = True
				elapsed+=eta
			else:
				elapsed+=c_arr[x]/income
				income+=f_arr[x]

		ans_arr.append(elapsed)

def write_stuff():
	with open("jamq2o.txt", 'w') as f:
		for x in xrange(len(ans_arr)):
			f.write("Case #" + str(x+1) + ": " + str(round(ans_arr[x], 7)) + '\n')

	f.close()

def main():
	read_file()
	calc_stuff()
	write_stuff()
			
main()