from sys import stdout
import re

i=0
counter=1
flag=0
error=0
mylist=list()


try:
    number=input()
except :
    print "Error: First line should be Number of Test Cases"
    number=0
    error=1

if(0 < number <= 50):
    while i<number:
        flag=0
        ab=raw_input()
        mylist.append(ab)
        i= i + 1

    for line in mylist:       
        count = 0
        flag=0
        stdout.write("Case #"+ str(counter)+": ")
        num=line.split()
        if len(num)<2 or len(num)>2:
            stdout.write("Error: Wrong Input")
        else:
            A=num[0]
            B=num[1]
            if not re.search('^[0-9]+$', A) or not re.search('^[0-9]+$', B):
                stdout.write("Error: Wrong Input")
                flag=1
            if len(A)!=len(B):
                stdout.write("Error: A and B should have the same number of digits.")
                flag=1
            if flag==0:
                if not 1<=int(A)<=int(B)<=1000:
                    stdout.write("Error: 1 <= A<= B<= 1000.")
                else:
                    if len(A)==2:
                        for n in range(int(A),int(B)+1):
                            p=str(n)
                            p = p[::-1]
                            if not p.startswith("0"):
                                if int(p)>n and int(p)<=int(B):
                                    count= count+1
                    if len(A)==3:
                        for n in range(int(A),int(B)+1):
                            k=str(n)
                            last = k[2:]
                            two=k[:2]
                            p=str(last)+str(two)
                            if not p.startswith("0"):
                                if int(p)>n and int(p)<=int(B):
                                    count= count+1
                        for n in range(int(A),int(B)+1):
                            k=str(n)
                            lasttwo = k[1:]
                            first=k[:1]
                            p=str(lasttwo)+str(first)
                            if not p.startswith("0"):
                                if int(p)>n and int(p)<=int(B):
                                    count= count+1
                            
        stdout.write(count)
        print
        counter = counter + 1
else:
    if error==0:
         print "Limit #1: 1 <= T <= 50. Where T is number of test cases"
   


        

