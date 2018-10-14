def findunflipped(string, flipper):               #this function will find the unflipped pancake from the center
    for i in range(len(string)):           #while on the wrong side
        if string[i] == "-":             #finding unflipped
            return [i, i + flipper - 1]

    
def flip(string, start, end):               #flip the string
    flipped_string = ""
    for i in range(start, end + 1):
        if string[i] == '-':
            flipped_string += '+'
        else:
            flipped_string += '-'
    return string[:start] + flipped_string + string[end+1:]
    
file = open("A-large.in", "r")
infile = [i.split() for i in file.readlines()]
test_cases = int(infile[0][0])
input_cases = []
newfile = open("GCI_1.txt", "w")
for j in range(1, test_cases + 1):          #first element is number of test cases (just checking that)
    input_cases.append(infile[j])
for j in range(len(input_cases)):
    flip_string = input_cases[j][0]
    flipper = int(input_cases[j][1])
    flip_no = 0
    while '-' in flip_string:
        curr_flipping_range = findunflipped(flip_string, flipper)
        flip_string_copy = flip_string              #storing the value to check if anything has changed later (ie impossible case
        if curr_flipping_range[1] >= len(flip_string):            #error case
            print ("Case #{0}: IMPOSSIBLE".format(j + 1))
            newfile.write("Case #{0}: IMPOSSIBLE\n".format(j + 1))
            break
        else:
            flip_string = flip(flip_string, curr_flipping_range[0], curr_flipping_range[1])
        if flip_string == flip_string_copy:
            print ("Case #{0}: IMPOSSIBLE".format(j + 1))
            newfile.write("Case #{0}: IMPOSSIBLE\n".format(j + 1))
            break
        flip_no += 1
    else:
        print ("Case #{0}: {1}".format(j + 1, flip_no))
        newfile.write("Case #{0}: {1}\n".format(j + 1, flip_no))
newfile.close()
