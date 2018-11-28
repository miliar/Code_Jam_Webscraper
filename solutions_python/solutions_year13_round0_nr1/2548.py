def checkx(s):
	return (s == 'XXXX' or s == 'XXXT' or s == 'XXTX' or s == 'XTXX' or s == 'TXXX')

def checko(s):
	return (s == 'OOOO' or s == 'OOOT' or s == 'OOTO' or s == 'OTOO' or s == 'TOOO')

n = int(input())
for i in range(n):
	s1 = input()
	s2 = input()
	s3 = input()
	s4 = input()
	s5 = s1[0] + s2[0] + s3[0] + s4[0]
	s6 = s1[1] + s2[1] + s3[1] + s4[1]
	s7 = s1[2] + s2[2] + s3[2] + s4[2]
	s8 = s1[3] + s2[3] + s3[3] + s4[3]
	s9 = s1[0] + s2[1] + s3[2] + s4[3]
	s10 = s1[3] + s2[2] + s3[1] + s4[0]
	if checkx(s1) or checkx(s2) or checkx(s3) or checkx(s4) or checkx(s5) or checkx(s6) or checkx(s7) or checkx(s8) or checkx(s9) or checkx(s10):
		ans = 'X won'
	elif checko(s1) or checko(s2) or checko(s3) or checko(s4) or checko(s5) or checko(s6) or checko(s7) or checko(s8) or checko(s9) or checko(s10):
		ans = 'O won'
	elif ('.' in s1) or ('.' in s2) or ('.' in s3) or ('.' in s4):
		ans = 'Game has not completed'
	else:
		ans = 'Draw'
	print('Case #' + str(i + 1) + ': ' + ans, end = '\n')
	s1 = input()
