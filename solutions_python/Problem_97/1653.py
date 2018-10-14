#!/usr/bin/python



file_in = open ('c:/Python27/recycled_input.txt','r')

inputlines = file_in.readlines()
file_in.close()

file_out=open('c:/Python27/recycled_solution.txt', 'w')

n=int(inputlines[0])

for test_case in range(1,n+1):

    data=inputlines[test_case].split()
    
    a=int(data[0])
    b=int(data[1])
    
    n=0
    
    for i in range(a,b):
        s=str(i)
        found=[]
        if len(s)>1:
            for j in range(1,len(s)):
                t=int(s[j:len(s)]+s[0:j])
                nfound=found.count(t)
                if (t>=a and t<=b and t>i and nfound==0):
                    found.append(t)
                    n=n+1   
    answer=n
    
    outstring = "Case #%d: %s\n" % (test_case, answer)

    print outstring
    
    file_out.write(outstring)
    
file_out.close()

    








    
    
    




