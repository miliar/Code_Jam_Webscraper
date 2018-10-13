def check(mat):
	for i in xrange(4):
		counter={'T':0,'O':0,'X':0,'.':0}
		for j in xrange(4):
			counter[mat[i][j]]+=1
		if (counter['O']==4) or (counter['O']==3 and counter['T']==1):
			return "O won"
		if (counter['X']==4) or (counter['X']==3 and counter['T']==1):
			return "X won"
	return None
def solve():
	mat=[0 for x in xrange(4)]
	for i in xrange(4):
		mat[i]=raw_input()
#check row:
	ret=check(mat)
	if ret:
		return ret;
	mat2=[[0]*4 for x in xrange(4)]
	for i in xrange(4):
		for j in xrange(4):	
			mat2[i][j]=mat[j][i]
			
	ret=check(mat2)
	if ret:
		return ret;	
	
	counter={'T':0,'O':0,'X':0,'.':0}
	for i in xrange(4):
		counter[mat[i][i]]+=1
	if (counter['O']==4) or (counter['O']==3 and counter['T']==1):
		return "O won"
	if (counter['X']==4) or (counter['X']==3 and counter['T']==1):
		return "X won"		
	counter={'T':0,'O':0,'X':0,'.':0}
	
	for i in xrange(4):
		counter[mat[i][4-i-1]]+=1
	if (counter['O']==4) or (counter['O']==3 and counter['T']==1):
		return "O won"
	if (counter['X']==4) or (counter['X']==3 and counter['T']==1):
		return "X won"
	if counter["."]>0:
		return "Game has not completed"
	return "Draw"
def main():
	cn=int(raw_input())
	for cs in xrange(cn):
		print "Case #%d: %s" % (cs+1,solve())
		if cs<cn-1:
			raw_input()
if __name__=="__main__":
	main()