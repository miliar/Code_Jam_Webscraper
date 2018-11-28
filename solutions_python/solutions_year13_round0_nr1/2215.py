import sys

X_won_pattern = ['XXXX','XXXT','XXTX','XTXX','TXXX']
O_won_pattern = ['OOOO','OOOT','OOTO','OTOO','TOOO']
def check_rows(mat,symbol):
	for row in mat:
		if symbol == 'X':
			if row in X_won_pattern:
				return True
		if symbol == 'O':
			if row in O_won_pattern:
				return True
	return False

def check_cols(mat,symbol):
	for i in range(4):
		col = ''
		for j in range(4):
			col=col+mat[j][i]
		if symbol == 'X':
			if col in X_won_pattern:
				return True
		if symbol == 'O':
			if col in O_won_pattern:
				return True			
	return False


def check_diag(mat,symbol):
	main_diag = mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3]
	#print main_diag
	opp_diag =  mat[0][3]+mat[1][2]+mat[2][1]+mat[3][0]
	#print opp_diag
	if symbol == 'X':
		if main_diag in X_won_pattern:
			return True
		if opp_diag in  X_won_pattern:
			return True
	if symbol == 'O':
		if main_diag in O_won_pattern:
			return True
		if opp_diag in  O_won_pattern:
			return True
	return False

def check_empty(mat):
	for row in mat:
		if row.find('.')!=-1:
			return True
	return False


oF = open(sys.argv[1])
oF1 = open('taskASolLarge.txt','w')

T = int(oF.readline().strip())

for i in range(T):
	mat = []
	for j in range(4):
		mat.append(oF.readline().strip().upper())
	oF.readline() #empty line 
	
	#check if x is wining
	if check_rows(mat,'X'):
		oF1.write('Case #%d: X won\n'%(i+1))
		continue
	if check_cols(mat,'X'):
		oF1.write('Case #%d: X won\n'%(i+1))
		continue
	if check_diag(mat,'X'):
		oF1.write('Case #%d: X won\n'%(i+1))
		continue
	#check if o is wining
	if check_rows(mat,'O'):
		oF1.write('Case #%d: O won\n'%(i+1))
		continue
	if check_cols(mat,'O'):
		oF1.write('Case #%d: O won\n'%(i+1))
		continue
	if check_diag(mat,'O'):
		oF1.write('Case #%d: O won\n'%(i+1))
		continue
	
	if check_empty(mat):
		oF1.write('Case #%d: Game has not completed\n'%(i+1))
		continue
	oF1.write('Case #%d: Draw\n'%(i+1))


