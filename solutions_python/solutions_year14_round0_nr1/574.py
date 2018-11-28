import sys

fi = open('magic.in', 'r')

T = int(fi.readline().rstrip('\n'))
for i in range(T):
		rows = []
		for j in range(2):
				row_num = int(fi.readline().rstrip('\n'))
				for k in range(1, 5):
						line = fi.readline().rstrip('\n')
						if k == row_num:
								rows.append(line)

		exist = {}
		for row in rows:
				vals = row.split(' ')
				for val in vals:
						if val in exist:
								exist[val] += 1
						else:
								exist[val] = 1
		res = []
		for key in exist:
				if exist[key] == 2:
						res.append(key)

		l = len(res)
		if l == 1:
				print 'Case #' + str(i+1) + ': ' + res[0]
		elif l == 0:
				print 'Case #' + str(i+1) + ': Volunteer cheated!'
		else:
				print 'Case #' + str(i+1) + ': Bad magician!'
