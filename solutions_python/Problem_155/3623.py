import sys;

def main():
	contents = [];
	with open(sys.argv[1], 'r') as f:
		contents = f.readlines();
	print_invite(contents);

def print_invite(contents):
	num = contents[0];
	f= open('result.txt', 'w');
	for i in range(1, int(num) + 1):
  		invite = find_num_invite(contents[i]);
  		f.write('Case #' + str(i) + ': ' + str(invite) + '\n');

def find_num_invite(shyness):
	num_aud = int(shyness[0]);
	array_shy = [shyness[i] for i in range(2, len(shyness) - 1)];
	array_shy = map(int, array_shy);
	num_stand = 0;
	last_stand = -1;
	invite = 0;
	for i in range(num_aud + 1) :
		if(num_stand >= i and array_shy[i] > 0):
			num_stand += array_shy[i];
			last_stand = i;
		elif(array_shy[i] > 0):
			missing = i - num_stand;
			while(missing > 0 and last_stand >= 0 and array_shy[num_stand] > 0):
				print missing;
				invite += missing / array_shy[num_stand];
				missing -= invite * array_shy[num_stand];
				num_stand += invite;
				last_stand -= 1;
			if(missing > 0) :
				invite += missing;
			last_stand = i;
			num_stand += array_shy[i] + invite;
			print invite;

	return invite;

if __name__ == '__main__':
    main();
