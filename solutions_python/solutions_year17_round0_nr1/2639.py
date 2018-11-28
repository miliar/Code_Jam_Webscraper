import sys

def flip(pan_array, flip_size, position):
    for i in xrange(flip_size):
        #print "index: " + str(i)
        #print "position: " + str(position)
        old_val = pan_array[position + i]
        new_val = "+" if old_val == "-" else "-"
        #print "old val: " + str(old_val)
        #print "new val: " + str(new_val)
        pan_array[position + i] = new_val

def solve(pan_array, flip_size):
    length = len(pan_array)
    flips = 0
    for i in xrange(length):
        if length - i < flip_size and "-" == pan_array[i]:
            #print "length: " + str(length)
            #print "i: " + str(i)
            #print "flip_size: " + str(flip_size)
            return "IMPOSSIBLE"
        if "-" == pan_array[i]:
            #print "flip size: " + str(flip_size)
            #print "before flip"
            #print pan_array
            flip(pan_array, flip_size, i)
            flips += 1
            #print "after flip"
            #print pan_array
            #print "num flips"
            #print flips
    return flips

input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i = 1
for line in stripped_input_lines[1:]:
    split_line = line.split()
    pan_array = split_line[0]
    flip_size = int(split_line[1])
    result = solve(list(pan_array), flip_size)
    print "Case #" + str(i) + ": " + str(result)
    i += 1
