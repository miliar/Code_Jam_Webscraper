"""
https://code.google.com/codejam/contest/2974486/dashboard#s=p3
"""

        
# Define the names of the input and output files.
input_file = "D-large.in"
output_file = "D-large.out"

# Open the input file in read mode and output file in write mode.
input = open(input_file, 'r')
output = open(output_file, 'w')

# Store the number of cases.
cases = input.readline()
cases = int(cases[:-1])

for case in range(cases):

    num_rocks = input.readline()[:-1]
    
    naomi = input.readline()[:-1]
    naomi = naomi.split()
    i = 0
    for rock in naomi:
        naomi[i] = float(rock)
        i += 1
        
    ken = input.readline()[:-1]
    ken = ken.split()
    i = 0
    for rock in ken:
        ken[i] = float(rock)
        i += 1
        
    naomi.sort()
    ken.sort()
    
    index = 0
    for rock in naomi:
        if rock < ken[0]:
            index += 1
        else:
            break
    
    #deceitful = len(naomi) - index
    deceitful = 0
    k_index = 0
    for i in range(index, len(naomi)):
        if naomi[i] > ken[k_index]:
            deceitful += 1 # CHECK THIS....I NEED 1 MORE
            k_index += 1
    
    n = 0
    k = 0
    
    for rock in naomi:
        while k < len(ken) and ken[k] < rock:
            k += 1
            
        if k == len(ken):
            break
        else:
            k += 1
            n += 1
            
    normal = len(naomi) - n
    
    output.write("Case #{}: {} {}\n".format(case+1, deceitful, normal))
        
        
        
        
        
        
        
        
    