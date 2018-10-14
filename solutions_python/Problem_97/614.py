import math


def numcyc(num,numofdig,numoftimes):
    
    rdig=num%(math.pow(10,numoftimes))
    num=int(num/(math.pow(10,numoftimes)))
    return int(rdig*math.pow(10,numofdig-numoftimes+1) +num)

"""A=10
B=40
Barr=[4,0]
count=0
for num in range (A,B):
    print "START FOR NUM " + num
    mainnum=num
    dig=int(math.log10(num))
    for i in range(0,dig):
        num2=numcyc(num,dig)
        print num2
        if(num2!=mainnum and num2<B):
            count = count +1
        num=num2

print count 

        if(rmdig==0):
            
            num=numcyc(num,numofdig,2)
            print "inside rmdig 0 num ret " + str(num) 
            ind=ind +1
        elif(rmdig<Barr[0]):
            num=numcyc(num,numofdig,2)
            print "inside rmdig < num ret " + str(num) 
            ind=ind+1
            
        else :
            num=numcyc(num,numofdig,1)
            print "inside rmdig else num ret " + str(num)
            
        numcyc(num,numofdig,numoftimes)
"""


file1=open("input2.txt",'r')
file2=open("output.txt",'w')
numofcases=int(file1.readline())
for index in range(0,numofcases):
    aandb=file1.readline().split()
    A=int(aandb[0])
    B=int(aandb[1])
    Barr=int(aandb[1][0])
    #A=185
    #B=944
    #Barr=9
    count=0
  #  print str(A) + "  " + str(B) + "  " + str(Barr)
    for num in range (A,B+1):
        numinc=[]
   #     print str(len(numinc))
        numofdig=int(math.log10(num))
    #    print "START for num " + str(num)
        mainnum=num
        ind=0
        while ind<numofdig:
            ind=ind+1
            numoftimes=1
            rmdig=num%10
            tempnum=num
            while(rmdig==0 or rmdig > Barr):
                if(tempnum==0):
                    break
                numoftimes=numoftimes+1
                ind=ind+1
                tempnum=tempnum/10
                rmdig=tempnum%10;
            num=numcyc(num,numofdig,numoftimes)
            if(num<=B and num>=A and num>mainnum):
                if(num not in numinc):
     #               print "found pair (" + str(mainnum) + ","+str(num) +")"
                    numinc.append(num)
                    count =count +1
    file2.write("Case #"+str(index+1)+": " +str(count)+"\n")
file2.close()
