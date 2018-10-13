# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:27:06 2017

@author: FireCracker
"""
def checkNumber(l):
    i=0
    flag = 0
    l = l[::-1]
    while(i < len(l)):
        if(i == len(l)-1):
            return 0
        if(l[i] > l[i+1]):
            return 1
        else:
            flag = 1
        i+=1
    if(flag == 1):
        return 0

ofile = open('output.out',"w")
with open('B-small-attempt15.in') as fp:
    T = int(fp.readline(1))
    fp.close()
i=1
l = list()
while(i<=T):
    fvalue = 0
    ofile = open('output.out',"w+")
    with open('B-small-attempt15.in') as fp:
        for line in fp:    
            if(fvalue == 0):
                fvalue+=1
                continue
            else:
                number = int(line)
                if(number < 10):
                    output = "Case #"+str(i)+": "+ str(number) + "\n"
                    ofile.write(output)
                else:
                    while(number > 0):
                        number_t = number
                        while(number_t > 0 ):
                            temp = number_t % 10
                            l.append(temp)
                            number_t = number_t // 10
                        flag = checkNumber(l)
                        if(flag == False):  
                            output = "Case #"+str(i)+": "+ str(number) + "\n"
                            ofile.write(output)
                            l = list()
                            break
                        else:
                            print(l)
                            l = list()
                            number = number - 1
                i+=1        
fp.close()
ofile.close()              