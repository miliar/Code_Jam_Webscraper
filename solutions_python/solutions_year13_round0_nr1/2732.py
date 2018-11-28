import re

T = input()
for testcase in range(1,T+1):
	lines = []
	for i in [1,2,3,4]:
		lines.append(raw_input())
	for i in range(4):
		s = lines[0][i]+lines[1][i]+lines[2][i]+lines[3][i]
		lines.append(s)
	d = lines[0][0]+lines[1][1]+lines[2][2]+lines[3][3];
	lines.append(d);
	d = lines[0][3]+lines[1][2]+lines[2][1]+lines[3][0];
	lines.append(d);
	msg = "Case #"+str(testcase)+": "
	found = False;
	for line in lines:
		if (found):
			break
		if (re.match("(XXXX|TXXX|XTXX|XXTX|XXXT)", line)):
			msg +="X won"
			found = True
			break
		if (re.match("(OOOO|TOOO|OTOO|OOTO|OOOT)", line)):
			msg +="O won"
			found = True
			break
	if (found==False):
		for line in lines:
			if (re.match("\.+", line)):
				msg +="Game has not completed"
				found = True
				break
	if (found==False):
		msg += "Draw"
	print msg
	raw_input()