import re

testcase = int(raw_input())
for i in range(1, testcase+1, 1):
		inp = raw_input()
		init = map(int, re.findall(r'\d+', inp))

		event_number = init[0]
		event_time = []
		for j in range(1, event_number+1, 1):
				event_time.append(init[j])
		
		event_time.sort(reverse=True)
		
		process = []
		for j in range(0, event_number, 1):
				for k in range(j+1, event_number, 1):
						if event_time[j] - event_time[k] != 0:
								process.append(event_time[j] - event_time[k])

		gcd_number = 0
		count = len(process)
		if count == 0:
				gcd_number = event_time[0]
		elif count == 1:
				gcd_number = process[0]
		else:
				for j in range(0, count-1, 1):
						if process[j] != 0 and process[j+1] != 0:
								if gcd_number == 0:
										gcd_number = process[j]

								def gcd(a,b):
										while(a!=0):
												if a<b:
														temp = a
														a = b
														b = temp
												a = a%b
										return b

								gcd_number = gcd(gcd_number, process[j+1])

		if event_time[0]%gcd_number != 0:
				output_y = gcd_number - (event_time[0]%gcd_number)
		else:
				output_y = 0

		print "Case #%d: %d" %(i, output_y)
