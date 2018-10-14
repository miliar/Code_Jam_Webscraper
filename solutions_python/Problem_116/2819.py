#! /usr/bin/python
import copy
ip=open('in.in','r')
op=open('out.out','w')

tf=False

def draw(ttt):
	ttt1=copy.deepcopy(ttt)
	for x in range(0,4):
		for y in range(0,4):
			if ttt1[x][y]=='.':
				return False
	return True

def rep_x(ttt):
	ttt1=copy.deepcopy(ttt)
	for x in range(0,4):
		for y in range(0,4):
			if ttt1[x][y]=='T':
				ttt1[x][y]='X'
			tf=True;
	return ttt1

def rep_y(ttt):
	ttt1=copy.deepcopy(ttt)
	for x in range(0,4):
		for y in range(0,4):
			if ttt1[x][y]=='T':
				ttt1[x][y]='Y'
			
	return ttt1





cases=int(ip.readline().rstrip())
won=False;
for x in range(0,cases):
	won=False;
	ttt=[list(ip.readline().rstrip()),list(ip.readline().rstrip()),list(ip.readline().rstrip()),list(ip.readline().rstrip())]
	tttx=rep_x(ttt)
	ttty=rep_y(ttt)
	print ttt,'\n',tttx,'\n',ttty
	for i in range(0,4):
		for j in range(0,4):
			el=tttx[i][j]
			if won==True:
				break;
			if el=='.':
				break;
			if i==0:
				if j==0:
					if el==tttx[i][j+1] and el==tttx[i][j+2] and (el==tttx[i][j+3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					elif el==tttx[i+1][j+1] and el==tttx[i+2][j+2] and (el==tttx[i+3][j+3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					elif el==tttx[i+1][j] and el==tttx[i+2][j] and (el==tttx[i+3][j]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
				elif j==3:
					if el==tttx[i+1][j] and el==tttx[i+2][j] and (el==tttx[i+3][j]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					elif el==tttx[i+1][j-1] and el==tttx[i+2][j-2] and (el==tttx[i+3][j-3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
				else:
					if el==tttx[i+1][j] and el==tttx[i+2][j] and (el==tttx[i+3][j]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					
			else:
				if j==0:
					
					if el==tttx[i][j+1] and el==tttx[i][j+2] and (el==tttx[i][j+3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
	
	for i in range(0,4):
		if tf==True:
			break;
		for j in range(0,4):
			el=ttty[i][j]
			if won==True:
				break;
			if el=='.':
				break;
			if i==0:
				if j==0:
					if el==ttty[i][j+1] and el==ttty[i][j+2] and (el==ttty[i][j+3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					elif el==ttty[i+1][j+1] and el==ttty[i+2][j+2] and (el==ttty[i+3][j+3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					elif el==ttty[i+1][j] and el==ttty[i+2][j] and (el==ttty[i+3][j]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
				elif j==3:
					if el==ttty[i+1][j] and el==ttty[i+2][j] and (el==ttty[i+3][j]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					elif el==ttty[i+1][j-1] and el==ttty[i+2][j-2] and (el==ttty[i+3][j-3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
				else:
					if el==ttty[i+1][j] and el==ttty[i+2][j] and (el==ttty[i+3][j]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;
					
			else:
				if j==0:
					if el==ttty[i][j+1] and el==ttty[i][j+2] and (el==ttty[i][j+3]):
						op.write("Case #"+str(x+1)+": "+el+" won"); won=True;

	if won==False:
		if draw(ttt):
			op.write("Case #"+str(x+1)+": Draw");
		else:
			op.write("Case #"+str(x+1)+": Game has not completed");
	op.write('\n')
	ip.readline()
		




