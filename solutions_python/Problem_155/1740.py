import math

testcase = int(raw_input())+1;

for test in range(1, testcase):
	maxcount = 0;
	inputcase = raw_input().split();
	number = inputcase[1];
	arr = list(number);
	arr = map(int,arr);
	for i in range(1, int(inputcase[0])):
		arr[i] = arr[i] + arr[i-1];
		defi = i - (arr[i-1] + maxcount);
		if defi > 0:
			maxcount = maxcount + defi;
	defi = int(inputcase[0]) - (arr[int(inputcase[0])-1] + maxcount);
	if defi > 0:
		maxcount = maxcount + defi;
	print('Case #' + str(test) + ': ' + str(int(maxcount)));
