#!/usr/bin/python

file = open('B-large-0.in')
output = open('B-large-0.out', 'w')
T = int(file.readline())

for i in range(1, T+1):
    current = file.readline().split()
    combine = {}
    index = 0
    for c in range(int(current[index])):
        index+=1
        combine[current[index][:-1]]=current[index][-1]
    index+=1
    destroy = []
    for c in range(int(current[index])):
        index+=1
        destroy.append(current[index])
    
    index+=2
    o = []
    for letter in current[index]:
        if len(o)==0:
            o.append(letter)
        else:
            if o[-1]+letter in combine.keys():
                o[-1] = combine[o[-1]+letter]
            elif letter+o[-1] in combine.keys():
                o[-1] = combine[letter+o[-1]]
            else:
                o.append(letter)
                for old in o[:-1]:
                    if(old+letter in destroy or letter+old in destroy):
                        o = []
                        break
    
    output.write("Case #"+str(i)+": "+'[')
    for letter in o[:-1]:
        output.write(letter+','+' ')
    if len(o)>0:
        output.write(o[-1]+']\n')
    else:
        output.write(']\n')
    
