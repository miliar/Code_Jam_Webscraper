import math 

def is_square (x):
    return (math.floor (math.sqrt (x)) ** 2) == x

def test_fair_square (x):
    # Is square, Is palyndrom, Squared is palyndrom
    x_sqrt_int = int (math.floor (math.sqrt (x)))
    return (str(x) == str(x)[::-1]) and (is_square (x)) and (str(x_sqrt_int) == str(x_sqrt_int)[::-1])

input_filename = "C-small-attempt0.in"
output_filename = "C-small-output.txt"

input_file = open (input_filename, "r")
output_file = open (output_filename, "w")

# Read number of test cases
t = int (input_file.readline ().strip ())

# Read T inputs
for test_case in range (t):
    # Read a and b
    (a, b) = input_file.readline ().strip ().split ()

    # Count fair and square numbers
    fair_squares_count = 0
    lower_bound = math.ceil (math.sqrt (float (a)))
    upper_bound = math.floor (math.sqrt (float (b)))
    
    test_number = lower_bound

##    print lower_bound
##    print upper_bound

    while test_number <= upper_bound:
        squared_test = int(test_number ** 2)
##        print "testing", test_number, squared_test, a, b, squared_test >= float(a), squared_test <= float(b), test_fair_square (squared_test)

        if ((squared_test >= float(a)) and (squared_test <= float(b)) and (test_fair_square (squared_test))):
            fair_squares_count += 1

        test_number += 1
    
    output_file.write ("Case #" + str (test_case + 1) + ": " + str(fair_squares_count) + "\n")
    


    

    # Write output
##    if sw_wins:
##        output_file.write ("Case #" + str (test_case + 1) + ": " + win_player + " won" + "\n")
##    elif sw_empty_elem:
##        output_file.write ("Case #" + str (test_case + 1) + ": " + "Game has not completed" + "\n")
##    else:
##        output_file.write ("Case #" + str (test_case + 1) + ": " + "Draw" + "\n")

input_file.close ()
output_file.close ()
