
import sys

def findTidyNumberLogic(InitNum, N,nlen):
    newNum=InitNum
    initDig=nlen-1
    for i in range(1,nlen):
        for j in range(1,11):
            newNum = int(newNum) + int(''.join('1' for l in range(1,initDig+1)))
            if newNum > N or newNum%10==0:
                newNum = int(newNum) - int(''.join('1' for m in range(1,initDig+1)))
                break
        initDig=initDig-1
        if initDig < 0:
            break
    return(newNum)
    
#################### starting logic ############################
def findTidyNumber(n,nlen):
  if nlen>1:
    max9= int(''.join('9' for j in range(1,nlen)))
  min1= int(''.join('1' for k in range(1,nlen+1)))
  minN = int(''.join( str(n)[:1] for k in range(1,nlen+1)))
  if n<10 or 9*min1==n:
        return n
  elif n>=max9 and n<min1:
        return max9
  elif n>=minN:
        return findTidyNumberLogic(minN, n,nlen)
  elif n<minN :
       return findTidyNumberLogic( int(''.join( str(int(str(n)[:1])-1) for k in range(1,nlen+1)))  , n,nlen)
  return ''


################## takes input and prints #####################
T = int(input().strip())
L=[]
for i in range( 1,T+1 ):
    N=int(input().strip())
    NLen=int(len(str(N)))
    pnum=findTidyNumber(N,NLen)
    L.append(pnum)

for p in range( 1,T+1 ):
   print("Case #"+ str(p)+": " +str(L[p-1]))



