import math

s = [item.rstrip('\n') for item in open('prob1in.txt','r').readlines()]
numcases = int(s[0])
text_file = open('prob1out.txt', 'w')
addnum = 0

def main(num, case):
	good = False
	r = num.split('/')
	r[1] = int(r[1])
	r[0] = int(r[0])
	for t in range(int(r[0]), 2, -1):
		if r[1] % t == 0 and r[0] % t == 0:
			r[1] = int(r[1])/t
			r[0] = int(r[0])/t
	for i in range(1,40):
		if float(float(r[0])/float(r[1])) >= 2 ** -i:
			final = i
			break
	for i in range(1,40):
		if r[1] == 2 ** i:
			good = True
			break
	if good:
		return 'Case #' + str(case) + ': ' + str(final)
	else:
		return 'Case #' + str(case) + ': impossible'

for t in range(0, numcases):
	text_file.write(main(s[1+t], t+1) + '\n')

text_file.close()