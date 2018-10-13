import math

f = open("3in.txt").read().split("\n")
writeF = open("3out.txt","w")

def addnumber(number):
    if number%2==0:
        numbers.append(number/2)
        numbers.append(number/2-1)
    else:
        numbers.append((number-1)/2)
        numbers.append((number-1)/2)
    # print numbers

def getnumber(number,people):
    count=0
    addnumber(number)
    sortednumbers=list(numbers)
    
    while(len(numbers)<people*2):
        if(sortednumbers[count]==0):
            i
        else:
            addnumber(sortednumbers[count])
        count+=1
        sortednumbers=list(numbers)
        sortednumbers.sort(reverse=True)
    # print "printing sorted number"
    # print sortednumbers
    return numbers[len(numbers)-1]
    
for i in range(1,(int)(f[0])+1):
    numbers=[]
    condition=f[i].split(" ")
    # print ("%d %d" %(int(condition[0]),int(condition[1])))
    temp=(getnumber(int(condition[0]),int(condition[1])))
    print "Case #%d:"%i,numbers[len(numbers)-2],temp
    #print numbers
    writeF.write("Case #%d: %d %d\n" %(i,numbers[len(numbers)-2],temp))
    # numbers.sort(reverse=True)