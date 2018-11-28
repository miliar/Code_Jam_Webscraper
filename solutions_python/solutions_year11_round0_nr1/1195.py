'''
Created on May 7, 2011

@author: mwaidyanatha
'''

def main():
    input = open('A-large (1).in', 'r')
    output = open('output.out','w')
    cases = int(input.readline())
    for case in range(0, cases):
        line = (input.readline()).split()
        buttons = (line.pop(0))
        count(line, buttons, case+1,output)

def count(line, buttons, case, output):
    time = 0
    O_pre = 1
    B_pre = 1
    O_time = 0
    B_time = 0
               
    for i in range (0, len(line) / 2):
        robot = line[i * 2]
        position = int(line[i * 2 + 1])
        if robot == 'B':
            position_diff = abs(position - B_pre)
            if (time - B_time) >= position_diff:
                time += 1
            elif (time - B_time) < position_diff:
                time += (position_diff - time + B_time)
                time += 1
            B_time = time
            B_pre = position    
        else:
            position_diff = abs(position - O_pre)
            if (time - O_time) >= position_diff:
                time += 1
            elif (time - O_time) < position_diff:
                time += (position_diff - time + O_time)
                time += 1
            O_pre = position
            O_time = time
    print "Case #"+str(case)+": "+str(time)
    
    output.write("Case #"+str(case)+": "+str(time)+"\n")
        

main()
