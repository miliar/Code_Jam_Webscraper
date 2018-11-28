#!/usr/bin/env python
import sys

def recycle(filename1,output_name1):
    file1=open(filename1,'r')
    lines=file1.readlines()
    
    file2=open(output_name1,'w')
    length=len(lines)
    total=int(lines[0].strip("\r\n"))
    index=1
    for i in range(total):
        record=lines[index].strip("\r\n").split(" ")
        left=int(record[0])
        right=int(record[1])
        value=0
        for j in range(left,right+1):
            value+=possible_recycle(left,right,j)
            
        file2.write("Case #%s: %s\n" %(i+1,value))    
        index=index+1
        

def possible_recycle(left,right,number1):
    """given left<=number1<=right,
    can you find a
    """
    count=0
    str1=str(number1)
    first_digit=int(str1[0]) #first_digit of the number1
    #print first_digit
    for i in range(1,len(str1)):
        digit=int(str1[i])
        #print digit
        if (digit!=0) and (digit>=first_digit):
            newstr=str1[i:]+str1[0:i]
            new_number=int(newstr)
            #print newstr
            if (new_number>number1) and (new_number<=right):
                print str1,"*",newstr
                count+=1
    return count
    
if __name__=="__main__":
    recycle(sys.argv[1],sys.argv[2])
