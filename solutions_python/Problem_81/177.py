# coding: shift-jis

import sys

f = file(sys.argv[1])

test_cnt = int(f.readline())

for case in range(test_cnt):
	n = int(f.readline())
	res = [list(f.readline()[:-1]) for _ in range(n)]
	#print res
	
	wps = []
	owps = []
	#oppcnts = []
	for team in range(n):
		win = 0
		loss= 0
		
		# WP
		for i in range(n):
			if res[team][i] == '1':
				win += 1
			elif res[team][i] == '0':
				loss += 1
		wp = float(win)/(loss+win)
		wps += [wp]
		#print wp
		
		# OWP
		owp = 0.0
		oppcnt = 0
		for i in range(n):
			if i == team: continue
			if res[team][i] == '.':
				continue
			oppcnt += 1
			
			win = 0
			loss= 0
			for j in range(n):
				if j == team: continue
				if res[i][j] == '1':
					win += 1
				elif res[i][j] == '0':
					loss += 1
			owp += float(win)/(loss+win)
		owp /= oppcnt
		#oppcnts += [oppcnt]
		
		owps += [owp]
		#print owp
	print 'Case #%d:'%(case+1)
	for team in range(n):
		#oowp = (sum(owps) - owps[team])/oppcnts[team]
		oowp = 0.0
		oppcnt = 0
		for i in range(n):
			if res[team][i] == '.':
				continue
			oppcnt += 1
			oowp += owps[i]
		oowp /= oppcnt
			
		#print wps[team],owps[team],oowp
		print '%0.7f'%(0.25*wps[team] + 0.5*owps[team] + 0.25*oowp)
		
