# standing ovation

f = open('A-large.in.txt')
f_out = open('output.txt', 'w')

he = f.read()

date = he.split('\n')

out = ''

cases = date.pop(0)

counter = 1

for case in date:
	if not case:
		continue
	res = ''
	he1 = case.split(' ')
	he2 = map(int, list(he1[1]))
	res = 0
	for entry in range(0,len(he2)):
		if(entry == 0):
			continue
		# print entry
		# print(he2[0:(entry)])
		# print('summe :' + str(sum(he2[0:entry])))
		diff = entry - sum(he2[0:(entry)])
		# print(' index : '  + str(entry) + ' diff : ' + str(diff))
		if(diff>0):
			he2[0] += diff
			res += diff

	out = out + 'Case #' + str(counter) + ': ' + str(res) + '\n'
	counter += 1

f_out.write(out)
f_out.close()