import sys
import re

input_arr = []
c_arr = []
f_arr = []
x_arr = []
ans_arr = []
n_arr = []
k_arr = []

tmp_n_arr = []
tmp_k_arr = []

no_cheat_arr = []
cheat_arr = []

def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

def read_file():

	with open("jamq4i.txt", 'r') as f:
		count = 0
		for line in f:
			if count != 0:
				# if (count - 1) % 3 != 0:
				if (count - 1) % 3 == 1:
					arr = line[:-1].split(" ")
					tmp_arr_n = []
					for x in xrange(len(arr)):
						tmp_arr_n.append(float(arr[x]))
					n_arr.append(tmp_arr_n)
				if (count - 1) % 3 == 2:
					arr = line[:-1].split(" ")
					tmp_arr_k = []
					for x in xrange(len(arr)):
						tmp_arr_k.append(float(arr[x]))
					k_arr.append(tmp_arr_k)
			count+=1
	f.close()


def write_stuff():
	with open("jamq4o.txt", 'w') as f:
		for x in xrange(len(cheat_arr)):
			f.write("Case #" + str(x+1) + ": " + str(cheat_arr[x]) + " " + str(no_cheat_arr[x]) + '\n')

	f.close()

def first_bigger(ele, arr):
	found = false
	min_ele = -1.0
	for x in xrange(len(arr)):
		if arr[x] > ele and not found:
			min_ele = arr[x]
			found = True
		elif arr[x] > ele and arr[x] < min_ele and found:
			min_ele = arr[x]

	return min_ele

def first_bigger2(ele, arr):
	for x in xrange(len(arr)):
		if arr[x] > ele:
			return x
	return -1

def no_cheating():
	for x in xrange(len(n_arr)):
		# arr1 = qsort1(n_arr[x])
		# arr2 = qsort2(k_arr[x])
		# print n_arr[x], k_arr[x]
		arr1 = sorted(n_arr[x])
		arr2 = sorted(k_arr[x])
		# print arr1, arr2
		score = 0
		for y in xrange(len(arr1)):
			min_ele = first_bigger2(arr1[y], arr2)
			if min_ele == -1:
				score+=1
			else:	
				arr2.remove(arr2[min_ele])
		no_cheat_arr.append(score)
		# print score
		# print ""

def arr_compare(arr1, arr2):
	for x in xrange(len(arr1)):
		if arr2[x] > arr1[x]:
			return False
	return True


def cheating():
	for x in xrange(len(n_arr)):

		arr1 = sorted(n_arr[x])
		arr2 = sorted(k_arr[x])

		while not arr_compare(arr1, arr2):
			arr1.remove(arr1[0])
			arr2.remove(arr2[-1])

		cheat_arr.append(len(arr1))


def main():
	read_file()
	# quicksort()
	no_cheating()
	cheating()
	write_stuff()
main()