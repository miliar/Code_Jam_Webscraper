#!/usr/local/bin/python

s1 = open('s1.txt','r')
contents = s1.read()
lines = contents.split('\n')
s1.close()
###
s2 = open('s2.txt','w')
###

number_of_cases = int(lines[0])
for i in range(1,number_of_cases+1):
    temp_line = lines[i].split()
    maxS = int(temp_line[0])
    S = temp_line[1]
    standing_count = 0
    counter = 0
    for j in range(maxS+1):        
        if standing_count >= j:
            standing_count += int(S[j])
        else:
            while standing_count < j:
                standing_count += 1
                counter += 1
            standing_count += int(S[j])
        #print(i,j,standing_count)
    s2.write('Case'+' #'+str(i)+': '+str(counter)+'\n')

s2.close()
input1 = input('end')
