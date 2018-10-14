#tidyNum


def printCase(i,result):

    print("Case #{}: {} ".format(i, result))



def untidy(number, position, newnum):
    pass
    
def checkpair(newnumA, digit, digit1):
    if newnumA[digit]<=newnumA[digit+1]:
        return True#if true carry on else deal with number

    else :
        sigDigit=(int(newnumA[digit])-1)

        if sigDigit==0:
            sigDigit="0"#need to go round again

        else:sigDigit=str(sigDigit)
        newnumB=newnumA[:digit]+sigDigit
        #print("numb",newnumB)
        
        for nums in range(digit+1, len(newnumA)):
                newnumB=newnumB[:nums]+"9"
        #print(newnumB,"nB")
        return newnumB
                
         
 
 
def checkbackA(newnumber):
    pass


def checkTidy(n):
      #newnum=""
      count=0
      for digit in range(len(n)-1):
        if int(n[digit]) <= int(n[digit+1]):#tidy
            #newnum=newnum+n[digit]
            count=count+1
            #print(count)
            if count==len(n)-1:
                #print("qllgood")
                printCase(i,n)
             #   print("tidy")
                return True

      else: return False
    


#==================
t=int(input())
count=0
result="?"

for i in range(1,t+1):
    n=input()#[str(s) for s in input().split(" ")]#,
    newnum=""
    ###dostuff
    #special case 1
    if len(n)==1:
        printCase(i,n)
        continue

    test=False#checkTidy(n)
    #if test==True:continue
    
    digit=0        #continue
    #else: #not tidy
    while test==False:
        while digit<len(n)-1:#==False:
         #   print (test, n,"test,n",digit)
            
          #for digit in range(len(n)-1):
            #print(digit, n)
            newnumA=n#n[digit]+n[digit+1]
            test= checkpair(newnumA,digit, digit+1)
            if test==True:
                  #carry on but shoul not happen...
              #  print("nexting")
                digit=digit+1   # pass#continue
            else:
               n=str(int(test))
               digit=0
               #print("breaking")
               #break #continue
                
                
    result=n         
        #printCase(i,"0")
    ##prnt answer
    printCase(i,result)#change n m accordingly
