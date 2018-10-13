import sys

class Event:
	def __init__(self, event_type, timestamp, station):	
		self.event_type = event_type
		self.timestamp = timestamp 
		self.station = station
	
	def __str__(self):
		return "{"+self.event_type+","+ str(self.timestamp)+","+ self.station+"}"

def time_to_min(time):
	[hr, min] = map(int, time.split(":"))
	return hr*60+min

def event_list_insert(event_list, event):
	place = 0
	for _event in event_list:
		if event.timestamp > _event.timestamp:
			place = place +1
		else:
			break
	#event_list.insert(place, event)
	if len(event_list)>place and event_list[place].timestamp==event.timestamp:
		if event_list[place].event_type == "A":
			event_list.insert(place+1, event)
		else:
			event_list.insert(place, event)
	else:
		event_list.insert(place, event)
		

def print_event_list(event_list):
	list_str = ""
	for _event in event_list:
		list_str = list_str + str(_event) +"->"
	
	print list_str

def main():
	file = sys.argv[1]
	fin = open(file, "r")
	fout = open("output.txt", "w")
	num_inputs = int(fin.readline())
	#print "num_inputs:", num_inputs
	for i in range(num_inputs):
		halt_time = int(fin.readline())
		#print "halt_time:", halt_time
		[num_A, num_B] = map(int, fin.readline().split(" "))
		#print "num_A, num_B:", num_A, num_B
		event_list = []
		for j in range(num_A):
			[dep, arrv] = map(time_to_min, fin.readline().split(" "))
			#print dep, arrv
			dep_event = Event("D", dep, "A")
			arrv_event = Event("A", arrv+halt_time, "B")
			event_list_insert(event_list, arrv_event) 
			event_list_insert(event_list, dep_event)			
		for j in range(num_B):
			[dep, arrv] = map(time_to_min, fin.readline().split(" "))
			#print dep, arrv
			dep_event = Event("D", dep, "B")
			arrv_event = Event("A", arrv+halt_time, "A")
			event_list_insert(event_list, arrv_event) 
			event_list_insert(event_list, dep_event)			
		
		print_event_list(event_list)
		event_list.reverse()
		
		num_train_station_A = 0
		num_train_station_B = 0
		train_needed_A = 0
		train_needed_B = 0 
		
		while len(event_list)>0:
			curr_event = event_list.pop()
			#print "curr_event:", curr_event	
			if curr_event.event_type=="A":
				if curr_event.station=="A":
					num_train_station_A = num_train_station_A +1
				else:
					num_train_station_B = num_train_station_B +1
				print num_train_station_A, num_train_station_B, train_needed_A, train_needed_B	
			if curr_event.event_type=="D":
				if curr_event.station == "A":
					if num_train_station_A>0:
						num_train_station_A = num_train_station_A -1
					else:
						train_needed_A = train_needed_A +1	
				if curr_event.station == "B":
					if num_train_station_B>0:
						num_train_station_B = num_train_station_B -1
					else:
						train_needed_B = train_needed_B +1
				print num_train_station_A, num_train_station_B, train_needed_A, train_needed_B	
		
		print "output:", train_needed_A, train_needed_B	
		fout.write("Case #"+str(i+1)+": "+ str(train_needed_A) +" "+ str(train_needed_B)+"\n")

if __name__ == "__main__":
    main()

