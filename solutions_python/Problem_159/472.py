#python 2.7

import sys

def solve(input_vals):
    const_rate = max( [ input_vals[x] - input_vals[x+1] for x in range(0,len(input_vals) - 1) ] )
    min_eaten_var_rate = sum( [ max([input_vals[x] - input_vals[x+1], 0]) for x in range(0,len(input_vals) - 1) ] )
    
    const_eaten = 0
    
    input_vals.pop()
    
    for plate in input_vals:
        print str(plate) + " vs " + str(const_rate)

        if plate < const_rate:
            const_eaten += plate
        else:
            const_eaten += const_rate
        print "Eaten= " + str(const_eaten)
        
    return str(min_eaten_var_rate) + " " + str(const_eaten)

def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        res = solve([ int(x) for x in split_input[2 + 2*(i)].split(" ") ])
        output_file.write("Case #" + str(i + 1) + ": " + res + "\n")
    
if __name__ == "__main__":
    main()
