from math import *

#checking for valid palindrome : returns boolean
def palindrome(num):
    string=str(num)
    return (string==string[::-1])

#process input and output to and from files
fin=open("inputl.in","r")
out=open("output.out","w")

array = []
for num in range(1,int(ceil(sqrt(100000000000000)))):
    if palindrome(num) and palindrome(num*num):
        array.append(num*num)
#print array


#number of test cases
test=int(fin.readline())
#print test

for i in range(0,test):
    start,end=fin.readline().split()
    start,end=int(start),int(end)
    count=0
    #print (i,start,end)
    for nn in range(0,len(array)):
        if (array[nn]>=start) and (array[nn]<=end):
            count+=1
    st="Case #"+str(i+1)+": "+str(count)+"\n"
    out.write(st)

fin.close()
out.close()
