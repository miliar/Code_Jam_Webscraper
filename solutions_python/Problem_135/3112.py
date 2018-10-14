lines = [line.strip() for line in open('/Users/jlinenthal/downloads/magic.in')]

n = int(lines[0])
idx=1
for i in range(1,n+1):
    guess = int(lines[idx])
    row = map(int,lines[idx+guess].split(' '))
    guess2 = int(lines[idx+5])
    row2 = map(int,lines[idx+5+guess2].split(' '))
    #print guess, guess2,row, row2
    z = set(row).intersection(row2)
    if len(z) == 0:
	print 'Case #' + str(i) + ': Volunteer cheated!'
    if len(z) == 1:
	print 'Case #' + str(i) + ': ' + str(list(z)[0])
    if len(z) > 1:
	print 'Case #' + str(i) + ': Bad magician!'
    idx += 10
