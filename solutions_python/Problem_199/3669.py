import re

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

def num_flips(row_of_pancakes, K):
    #itterate over row of pancakes. Everytime you come across a pancake which is the wrong way around,
    # flip it, but without affecting the correct pancakes to the left
    flip_count = 0
    #first turn string into list
    row = list(row_of_pancakes);

    for i, pancake in enumerate(row):
        if(pancake != '+'):

            #flip it and K-1 more after it
            try:
                for j in range(0,K):
                    if(row[i+j] == '+'):
                        row[i + j] = '-'
                    elif(row[i+j] == '-'):
                        row[i + j] = '+'
                    else:
                        print("Something wrong!")
                #after flipping, increment flip counter
                flip_count = flip_count + 1
            except IndexError:
                return(-1)

    return (flip_count)



input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

number_of_lines = int(input_file.readline())
print("%d lines" %(number_of_lines))

for i in range(0,number_of_lines):
    line = input_file.readline()
    line = line.rstrip()

    K = get_trailing_number(line)
    line = line.split(" ", 1)[0]
    flips_required = num_flips(line, K)
    print("Processing line %d" %(i+1))
    if (flips_required == -1):
        output_file.write("Case #%s: %s\n" % (str(i + 1), "IMPOSSIBLE"))
    else:
        output_file.write("Case #%s: %d\n" %(str(i + 1), flips_required))

#close files
input_file.close()
output_file.close()