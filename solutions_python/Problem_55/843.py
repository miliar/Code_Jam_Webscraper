'''
Created on May 7, 2010

@author: kapild
'''

from math import pow

def SnapperChain(fileName):
    
    fr = open(fileName)
    
    lines = fr.readline()
    
    input = fr.readlines()
    
    total_run = int(lines) * 2

    for i in range(0,total_run,2):

        input_line = input[i].split(" ")
        
        total_run = int(input_line[0])
        max_seat = int(input_line[1])
        no_grps = int(input_line[2])

        groups = input[i+1].split(" ")

#        print 'total_run:' + str(total_run) + " max_seat:" + str(max_seat) + "no_grps" + str(no_grps) + str(groups)

        if (len(groups) != no_grps):
            print "bad"
            break 
            
        money_earned = 0
        index= 0
        max_index = no_grps        
        start=0
        for run in range(total_run):
            sum = 0            
            while(True):
                index = getI(index, max_index)
                
                if(sum + int(groups[index]) <= max_seat):
                    sum+=int(groups[index])
                    money_earned+=int(groups[index])
                    if(getI(index + 1, max_index) == start):
                        index+=1
                        index=getI(index, max_index)
                        start = index
                        break
                    else:
                        index+=1
                        index=getI(index, max_index)
                else:
                    start=index
                    break
                
            
        print "Case #"+ str((i+2)/2) + ": " + str(money_earned)
    

def getI(index, max):
    if( index <= max -1):
        return index
    else:
        return 0 

if __name__ == '__main__':

    SnapperChain("theme.txt")