def narrow_down(departures, arrivals, T):
	departures.sort()
	arrivals.sort()
	arrivals.reverse()
	reusable = 0
	for arrival in arrivals:
		i = find_smallest(departures, arrival + T)
		if i != -1:
			departures.pop(i)
		

def find_smallest(l, num):
	for i, item in enumerate(l):
		if num <= item:
			return i
	return -1

def count_trains(A_table, B_table, T):
	A_times = []
	for item in A_table:
		depart, arrive = map(conv_time, item.strip().split(" "))
		A_times.append((depart, arrive))
	B_times = []
	for item in B_table:
		depart, arrive = map(conv_time, item.strip().split(" "))
		B_times.append((depart, arrive))
	A_depart = [time[0] for time in A_times]
	A_arrive = [time[1] for time in B_times]
	B_depart = [time[0] for time in B_times]
	B_arrive = [time[1] for time in A_times]
	narrow_down(A_depart, A_arrive, T)
	narrow_down(B_depart, B_arrive, T)
	return ( len(A_depart), len(B_depart))

def conv_time(s):
	hours, minutes = map(int, s.strip().split(":"))
	return hours*60 + minutes

def main():
	from sys import argv
	input_file = open(argv[1]).readlines()
	num_cases = int(input_file[0])
	input_file = input_file[1:]
	for case in range(1, num_cases+1):
		T = int(input_file[0])
		input_file = input_file[1:]
		a_num, b_num = map(int, input_file[0].strip().split(" "))
		input_file = input_file[1:]
		A_table = input_file[:a_num]
		B_table = input_file[a_num:a_num+b_num]
		input_file = input_file[a_num + b_num:]
		a, b = count_trains(A_table, B_table, T)
		print "Case #%d: %d %d" % (case, a, b)

if __name__=="__main__":
	main()
