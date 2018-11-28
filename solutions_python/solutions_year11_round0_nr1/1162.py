import sys

def self():
	time_taken_O = 0;
	time_taken_B = 0;
	position_O = 1;
	position_B = 1;
	time = 0
	push = 1

	filename = 'test.in'
	if len(sys.argv)==2:
		filename = sys.argv[1]
	out = filename[:-3]+'.out'
	print out
	f = open(filename)
	w = open(out, 'w')
	tests = int(f.readline())

	i = 0
	while i < tests:
		print i
		i = i+1
		line = f.readline()
		pieces = line.split(' ')
		print pieces
		buttons = pieces[0]
		j = 1
		
		time = 0
		time_taken_O = 0;
		time_taken_B = 0;
		position_O = 1;
		position_B = 1;
		
		while j < len(pieces):
			color = pieces[j]
			button = int(pieces[j+1])
			print color,button
			if color == 'O':
				time_used = abs(position_O - button) - time_taken_B
				position_O = button
				if time_used < 0:
					time_used = 0
				time_used = time_used + push
				time_taken_O = time_taken_O + time_used
				time_taken_B = 0
				time = time + time_used
				print time
			if color == 'B':
				time_used = abs(position_B - button) - time_taken_O
				position_B = button
				if time_used < 0:
					time_used = 0
				time_used = time_used + push
				print 'time used = ',time_used
				time_taken_B = time_taken_B + time_used
				time_taken_O = 0
				time = time + time_used
				print time
			print time_taken_O, time_taken_B
			j = j+2
		w.write('Case # '+str(i)+':'+str(time)+'\n')


if __name__ == "__main__":
	self()
