import sys
import string

block=[]


def main():
    f=open(sys.argv[1],'r')
    num=f.readline()
    num=int (num)
    countd=0
    counto=0
    countx=0
    count=0
    result=' '
    for g in range(0,num):
        one=f.readline()
        one=one.rstrip()
        two=f.readline()
        two=two.rstrip()
        three=f.readline()
        three=three.rstrip()
        four=f.readline()
        four=four.rstrip()
        block.append([one,two,three,four])
        #print block
        f.readline()
        countd=0
   	result=' '
	for i in range (0,4):
		countx=0
		counto=0
		for j in range (0,4):
			if(block[0][i][j]=='X' or block[0][i][j]=='T'):
				countx+=1
				
			if(block[0][i][j]=='O' or block[0][i][j]=='T'):
				counto+=1	
				
			if(block[0][i][j]=='.'):
				countd+=1			
	
		
		if(countx==4):
			result='X'
		if(counto==4):
			result='O'	
		
	
	for j in range (0,4):
		countx=0
		counto=0
		for i in range (0,4):
			if(block[0][i][j]=='X' or block[0][i][j]=='T'):
				countx+=1
			if(block[0][i][j]=='O' or block[0][i][j]=='T'):
				counto+=1				
		
		if(countx==4):
			result='X'
		if(counto==4):
			result='O'	
	
	
	countx=0
	counto=0
	for i in range (0,4):
		if(block[0][i][i]=='X' or block[0][i][i]=='T'):
			countx+=1	
		if(block[0][i][i]=='O' or block[0][i][i]=='T'):
			counto+=1
		
		
	if(countx==4):
		result='X'
	if(counto==4):
		result='O'
			
			
	
	countx=0
	counto=0			
	
	for i in range (0,4):
		for j in range (0,4):
			if((i+j)==3):
				if(block[0][i][j]=='X' or block[0][i][j]=='T'):
					countx+=1
				if(block[0][i][j]=='O' or block[0][i][j]=='T'):
					counto+=1
			
		
		if(countx==4):
			result='X'
		if(counto==4):
			result='O'	
			
	if(result==' ' and countd==0):
		result='d'
	if(result==' ' and countd!=0):
		result='f'		
	
	if(result=='X'):
		print 'Case #'+str(g+1)+': X won'
	if(result=='O'):
		print 'Case #'+str(g+1)+': O won'
	if(result=='d'):
		print 'Case #'+str(g+1)+': Draw'
	if(result=='f'):
		print 'Case #'+str(g+1)+': Game has not completed'

	block.pop(0)
	
    
if __name__== '__main__':
    main()
