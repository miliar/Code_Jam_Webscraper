import sys;
import math;

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

for case in range(T):
	input = f_ip.readline().split();
	input.reverse();
	N = int(input.pop());
	
	spare = input[:];
	orange_seq = [];
	bloo_seq = [];
	Time = 0;

	for tot_buttons in range(N):
		curr_bot = input.pop();
		if curr_bot == 'O':
			orange_seq.append(int(input.pop()));
		else:
			bloo_seq.append(int(input.pop()));

	orange_pos = 1;
	bloo_pos = 1;
	orange_seq.reverse();
	bloo_seq.reverse();

#	print "----";

	for tot_buttons in range(N):
		curr_bot = spare.pop();
		spare.pop();
		
		if curr_bot == 'O':

			destination = orange_seq.pop();
			displacement = destination-orange_pos;
			shift = int(math.fabs(displacement));
#			print "Orange moved from ", orange_pos, "to",  destination, "at time",
			orange_pos = destination;
			Time = Time + shift + 1;
#			print Time;

			if len(bloo_seq):
				rival_dest = int(bloo_seq[-1]);
				bloo_displacement = rival_dest-bloo_pos;
				if bloo_displacement >= 0:	# Downstream
					if (shift + 1) < bloo_displacement:	# Bloo has to get far
						bloo_pos = bloo_pos + (shift + 1);
					else:
						bloo_pos = rival_dest;
				else:				# Upstream
					if (shift + 1) < (-bloo_displacement):
						bloo_pos = bloo_pos - (shift + 1);
					else:
						bloo_pos = rival_dest;
#				print "In the mean time Bloo moved to ", bloo_pos;

		else:	# Bloo Robot

			destination = bloo_seq.pop();
			displacement = destination-bloo_pos;
			shift = int(math.fabs(displacement));
#			print "Bloo moved from ", bloo_pos, "to",  destination, "at time",
			bloo_pos = destination;
			Time = Time + shift + 1;
#			print Time;

			if len(orange_seq):
				rival_dest = int(orange_seq[-1]);
				orange_displacement = rival_dest-orange_pos;
				if orange_displacement >= 0:	# Downstream
					if (shift + 1) < orange_displacement:		# Orange has to get far
						orange_pos = orange_pos + (shift + 1);
					else:
						orange_pos = rival_dest;
				else:				# Upstream
					if (shift + 1) < (-orange_displacement):
						orange_pos = orange_pos - (shift + 1);
					else:
						orange_pos = rival_dest;

#				print "In the mean time Orange moved to ", orange_pos;

	print "Case #" + str(case+1) + ":",
	print Time;