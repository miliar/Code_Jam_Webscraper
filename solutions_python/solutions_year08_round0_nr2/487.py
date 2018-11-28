import sys
from datetime import time

class test_case(object):
	def __init__(self, turnaround, travel_list_a, travel_list_b):
		self.__turnaround = turnaround
		self.__travel_list_a = travel_list_a
		self.__travel_list_b = travel_list_b

		self.__depart_timeline = []

		self.__arrival_timeline_a = []
		self.__arrival_timeline_b = []

		self.__train_count_a = 0
		self.__train_count_b = 0

		self.__total_train_count_a = 0
		self.__total_train_count_b = 0
		return

	def __get_travel_list_item_key(self, item):
		(d, a) = item
		return d

	def analyze(self):
		for (d, a) in self.__travel_list_a + self.__travel_list_b:
			#if not d in self.__depart_timeline:
			self.__depart_timeline.append(d)
		self.__depart_timeline.sort()
		self.__travel_list_a.sort(key = self.__get_travel_list_item_key)
		self.__travel_list_b.sort(key = self.__get_travel_list_item_key)
		return

	def run(self):
		for t in self.__depart_timeline:

			arrived_indexes_list = []
			for i in xrange(len(self.__arrival_timeline_a)):
				at = self.__arrival_timeline_a[i]
				if t == at or t > at:
					self.__train_count_a += 1
					arrived_indexes_list.insert(0, i)
			for i in arrived_indexes_list:
				del self.__arrival_timeline_a[i]

			arrived_indexes_list = []
			for i in xrange(len(self.__arrival_timeline_b)):
				at = self.__arrival_timeline_b[i]
				if t == at or t > at:
					self.__train_count_b += 1
					arrived_indexes_list.insert(0, i)
			for i in arrived_indexes_list:
				del self.__arrival_timeline_b[i]


			if self.__travel_list_a and t == self.__travel_list_a[0][0]:
				am = self.__travel_list_a[0][1].minute
				ah = self.__travel_list_a[0][1].hour
				at = self.__travel_list_a[0][1].replace(minute = (am +
					self.__turnaround) % 60, hour = ah + ((am + self.__turnaround) / 60))

				if(self.__train_count_a > 0):
					self.__train_count_a -= 1
				else:
					self.__total_train_count_a += 1

				self.__arrival_timeline_b.append(at)
				del self.__travel_list_a[0]

			if self.__travel_list_b and t == self.__travel_list_b[0][0]:
				am = self.__travel_list_b[0][1].minute
				ah = self.__travel_list_b[0][1].hour
				at = self.__travel_list_b[0][1].replace(minute = (am +
					self.__turnaround) % 60, hour = ah + ((am + self.__turnaround) / 60))

				if(self.__train_count_b > 0):
					self.__train_count_b -= 1
				else:
					self.__total_train_count_b += 1

				self.__arrival_timeline_a.append(at)
				del self.__travel_list_b[0]


		return (self.__total_train_count_a, self.__total_train_count_b)

def process_case(index, file):
	turnaround = int(file.readline())
	travel_list_list = [[], []]
	travel_count_list = []
	for s in file.readline().strip().split():
		travel_count_list.append(int(s))

	for i in xrange(2):
		n = travel_count_list[i]
		travel_list = travel_list_list[i]
		for j in xrange(n):
			t = file.readline().strip().split()
			d = t[0]
			a = t[1]
			travel_list.append((time(int(d[0:2]), int(d[3:5])),
				time(int(a[0:2]), int(a[3:5]))))

	tc = test_case(turnaround, travel_list_list[0], travel_list_list[1])
	tc.analyze()	
	r = tc.run()
	print 'Case #%i: %i %i' % (index, r[0], r[1])
	return

def main(argv):
	for input_file_name in argv:
		input_file = open(input_file_name, 'r')
		try:
			n = int(input_file.readline())
			for i in xrange(n):
				process_case(i + 1, input_file)
		finally:
			input_file.close()
	return

if __name__ == '__main__':
	#import pdb
	#pdb.set_trace()
	main(sys.argv[1:])
