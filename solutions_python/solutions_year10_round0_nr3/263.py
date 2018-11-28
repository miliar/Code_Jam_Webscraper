import sys
sys.stdin = open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\Qualification Round\C-small.in')
def giveSum(R,k,n,a):
    totalSum = 0
    i = 0
    numRides = 0
    while True:
        rideSum = 0
        if(numRides!=0 and i==0 and ((R-numRides)>=numRides)):
            totalSum = (R//numRides) * totalSum
            numRides = (R//numRides) * numRides
        numG = 0
        if(R == numRides):
            break
        while(a[i]+rideSum<=k and numG<n):
            rideSum += a[i]
            i = (i+1)%n
            numG+=1
        numRides+=1
        totalSum+=rideSum
    return totalSum
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\Qualification Round\C-small.out',mode='w')
t = int(input())
for i in range(1,t+1):
    R,k,n = [int(i) for i in input().split()]
    g = [int(i) for i in input().split()]
    print('Case #{0}: {1}'.format(i,giveSum(R,k,n,g)),file=output)
output.close()
