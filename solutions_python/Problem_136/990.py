"""
https://code.google.com/codejam/contest/2974486/dashboard#s=p1
"""

        
# Define the names of the input and output files.
input_file = "B-large.in"
output_file = "B-large.out"

# Open the input file in read mode and output file in write mode.
input = open(input_file, 'r')
output = open(output_file, 'w')

# Store the number of cases.
cases = input.readline()
cases = int(cases[:-1])

for case in range(cases):

    info = input.readline()[:-1]
    info = info.split()
    
    C = float(info[0])
    F = float(info[1])
    X = float(info[2])
       
    farm_time = 0
    rate = 2   
    completion_time = X / rate
    
    while 1:
        farm_time += C / rate
        rate += F
        
        if (completion_time) > (farm_time + (X / rate)):
            completion_time = farm_time + (X / rate)
            continue
        else:
            break
        
    output.write("Case #{}: {}\n".format(case+1, completion_time))
    
    
    
