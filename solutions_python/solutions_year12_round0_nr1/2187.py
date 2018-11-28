#!/usr/bin/python



file_in = open ('c:/Python27/tongues_input.txt','r')
inputlines = file_in.readlines()
file_in.close()

file_out=open('c:/Python27/tongues_solution.txt', 'w')

inputcode = 'abcdefghijklmnopqrstuvwxyz\n '
outputcode= 'yhesocvxduiglbkrztnwjpfmaq\n '

n=int(inputlines[0])

for test_case in range(1,n+1):


    data=inputlines[test_case].rstrip()

   # print data
    
    answer=''
    
    for i in data:
        answer += outputcode[inputcode.find(i)]

    outstring = "Case #%d: %s\n" % (test_case, answer)

    print outstring
    
    file_out.write(outstring)
    

file_out.close()

    








    
    
    




