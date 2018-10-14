"""
https://code.google.com/codejam/contest/2974486/dashboard#s=p0
"""

        
# Define the names of the input and output files.
input_file = "A-small-attempt0.in"
output_file = "A-small-attempt0.out"

# Open the input file in read mode and output file in write mode.
input = open(input_file, 'r')
output = open(output_file, 'w')

# Store the number of cases.
cases = input.readline()
cases = int(cases[:-1])

for case in range(cases):

    row1 = int(input.readline()[:-1])
    grid1 = []
    for i in range(4):
        grid1.append(input.readline()[:-1])
    
    row2 = int(input.readline()[:-1])
    grid2 = []
    for i in range(4):
        grid2.append(input.readline()[:-1])

    first_row = grid1[row1-1]
    second_row = grid2[row2-1]

    first_row = first_row.split()
    second_row = second_row.split()

    count = 0
    nums = []
    for num in second_row:
        if num in first_row:
            count += 1
            nums.append(num)
            
    if count == 0:
        output.write("Case #{}: Volunteer cheated!\n".format(case+1))
    elif count == 1:
        output.write("Case #{}: {}\n".format(case+1, nums[0]))
    elif count > 1:
        output.write("Case #{}: Bad magician!\n".format(case+1))
    
    
