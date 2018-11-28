import sys
import math    
inputFile=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\a-small.in')
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\a-small.out',mode='w')
sys.stdin = inputFile
c = int(input())
for i in range(1,c+1):
    l,p,c = [int(i) for i in input().split()]
    count =0
    while(l<p):
        l=c*l
        count+=1
    ans=int(math.ceil(math.log(count,2)))
    print('Case #{0}: {1}'.format(i,ans),file=output)
output.close()
inputFile.close()
