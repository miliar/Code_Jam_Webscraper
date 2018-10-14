# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def calcAudience(shyness):
    
    cdf = [0 for i in range(len(shyness))]
    cdf[0] = shyness[0]
    num_people = 0 
    for i in range(1, len(shyness)):
        cdf[i] = cdf[i - 1] + shyness[i]
        if cdf[i - 1] < i and shyness[i] > 0:
            num_people += i - cdf[i - 1]
            cdf[i] += num_people
            
    
    return num_people

# <codecell>

def readInput(file_name):
    file_reader = open(file_name, 'r')
    file_writer = file('output.txt','w')
    lines = file_reader.readlines()
    T = int(lines[0])
    for i in range(1, len(lines)):
        max_shyness = lines[i].split()[0]
        shyness = [int(s) for s in lines[i].split()[1]]
        
        num_people = calcAudience(shyness)
        file_writer.write("Case #" + str(i) + ": "+ str(num_people) + "\n")
        
    file_reader.close()
    file_writer.close()

# <codecell>

readInput('A-small-attempt1.in')

# <codecell>


