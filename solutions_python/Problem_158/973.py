import math
testcase = int(raw_input())+1;

for test in range(1, testcase):
	stats = raw_input().split();
	stats = map(int,stats);
	if stats[0] > 3 and stats[1]*stats[2] < 12:
		print('Case #' + str(test) + ': RICHARD');
	elif ((stats[1]*stats[2])%stats[0]) != 0:
                print('Case #' + str(test) + ': RICHARD');
	elif math.ceil(float(stats[0])/2) > stats[1] or math.ceil(float(stats[0])/2) > stats[2]:
                print('Case #' + str(test) + ': RICHARD');
        elif stats[0] > stats[1] and stats[0] > stats[2]:
                print('Case #' + str(test) + ': RICHARD');
	else:
                print('Case #' + str(test) + ': GABRIEL');
