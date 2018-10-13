import math
f = open('Input.txt')
lines = f.readlines()
f.close()
global_cnt = 0

def min_pi(Pi):
    Pi_to_pop = []
    highest_Pi = Pi[0]
    num_highest = 0
    second_highest = 0
    Pi_2 = []
    for j in range(len(Pi)):
        if(Pi[j] > highest_Pi):
            highest_Pi = Pi[j]
    for j in range(len(Pi)):
        if(Pi[j] == highest_Pi): 
            num_highest += 1
            Pi_to_pop.append(j)
    print Pi_to_pop
    print Pi
    for j in range(len(Pi_to_pop)):
        #print len(Pi_to_pop)-j-1
        Pi.pop(Pi_to_pop[len(Pi_to_pop)-j-1])      
    for j in range(len(Pi)):  #get second highest after popping highest but before putting on halves
        if(Pi[j] > second_highest):
            second_highest = Pi[j]
    for j in range(len(Pi)):  #try 6, 3 split for 9
        Pi_2.append(Pi[j])

    for j in range(len(Pi_to_pop)):
        if(highest_Pi != 1):
            Pi.append((highest_Pi)/2)
            Pi.append((highest_Pi)/2+highest_Pi%2)  
            if(highest_Pi == 9):
                Pi_2.append((highest_Pi)/3)
                Pi_2.append((highest_Pi)*2/3)
            else:
                Pi_2.append((highest_Pi)/2)
                Pi_2.append((highest_Pi)/2+highest_Pi%2)
    print Pi
    print highest_Pi
    print num_highest
    if((len(Pi) == 0)):
        return 1
    elif(highest_Pi == 2):
        return 2
    elif(highest_Pi == 3):
        return 3
    elif(highest_Pi == 9):
        if(num_highest == 1):
            if(second_highest <= 3):
                return 5
            else:
                return min(highest_Pi, num_highest + min_pi(Pi), num_highest + min_pi(Pi_2))                  
        else:
            return min(highest_Pi, num_highest + min_pi(Pi), num_highest + min_pi(Pi_2))            
    else:
        return min(highest_Pi, num_highest + min_pi(Pi))


output = open('BOutput.txt','w')

for i in range(int(lines[0])):
    D = int(lines[2*i+1])
    Pi = lines[2*i+2].split()
    for j in range(len(Pi)):
        Pi[j] = int(Pi[j])
    print "test",
    print i+1
    print "D ",
    print D
    print "Pi ",
    print Pi

    Minutes = min_pi(Pi)
    print "Minutes ",
    print Minutes
    output.write("Case #")
    output.write(str(i+1))
    output.write(": ")
    output.write(str(Minutes))
    output.write("\n")
        
output.close()         