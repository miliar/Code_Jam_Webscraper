import sys
inputFile = open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\Qualification Round\A-large.in')
sys.stdin = inputFile
def giveState(n,k):        
	state = 'OFF'
	k+=1
	if(k&((k>>n)<<n)==k):
		state = 'ON'
	return state
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\Qualification Round\A-large.out',mode='w')
t = int(input())
for i in range(1,t+1):
    n,k = [int(i) for i in input().split()]
    print('Case #{0}: {1}'.format(i,giveState(n,k)),file=output)
output.close()
inputFile.close()
