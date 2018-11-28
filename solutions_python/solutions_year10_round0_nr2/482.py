import functools
import sys
inputFile=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\Qualification Round\B-large.in')
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\Qualification Round\B-large.out',mode='w')
sys.stdin = inputFile
def gcd(a,b):	
	if a == 0:
		return b
	return abs(gcd(b % a, a))
    
def giveSlarboT(timeElapsed):
    k=[i[0]-i[1] for i in zip(timeElapsed[:-1],timeElapsed[1:])]
    k.append(timeElapsed[0]-timeElapsed[-1])
    commonDivisor = functools.reduce(gcd,k)
    if(commonDivisor==0):
        return 0
    rem = timeElapsed[0]%commonDivisor
    if(rem==0):
        return 0
    else:
        return commonDivisor- rem
c = int(input())
for i in range(1,c+1):
    greatEvents = [int(i) for i in input().split()]
    greatEvents = greatEvents[1:]
    print('Case #{0}: {1}'.format(i,giveSlarboT(greatEvents)),file=output)
output.close()
inputFile.close()
