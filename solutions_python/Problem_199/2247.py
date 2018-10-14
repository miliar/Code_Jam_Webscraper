
def mapToBoolean(input1):
    result=[True]*len(input1)
    for i in range(0,len(input1)):
        if(input1[i]=='-'):
            result[i]=False
    
    return result


def findTotalFlips(input1,k):
    count=0
    input1=mapToBoolean(input1)
    for i in range(0,len(input1)-k+1):
        if(not input1[i]):
            count+=1
            for j in range(i,i+k):
                input1[j]=not input1[j]
    for i in range(len(input1)-k,len(input1)):
        if(not input1[i]):
            return "IMPOSSIBLE"
    return count

t=int(input())
for i in range(1,t+1):
    temp=input()
    temp=temp.split()
    input1=temp[0]
    k=int(temp[1])
    print('Case #{}: {}'.format(i,findTotalFlips(input1,k)))
