f = open('A-large.in')
fw = open('A-large-output.txt', 'w')

cases = int(f.readline())
for case in range(cases):
	req_now = 0
	have_now = 0
	need_more = 0
	smax, aud = f.readline().split()
	for i in range(int(smax) + 1):
		req_now += 1
		have_now += int(aud[i])
		if have_now < req_now:
			need_more += (req_now - have_now)
			have_now = req_now

	fw.write('Case #' + str(case + 1) + ': ' + str(need_more) + '\n')

fw.close()
f.close()
