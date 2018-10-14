import sys
import time
from decimal import *

def open_io_files():
    assert len(sys.argv) > 1, "Error: missing input file name argument."

    try:
        input_filename = sys.argv[1]
        file_in = open(input_filename, "r")
        print "Opening file \"%s\" in read." %  input_filename
    except:
        assert False, "Error, could not read file \"%s\"." % input_filename

    if len(sys.argv) > 2:
        try:
            output_filename = sys.argv[2]
            file_out = open(output_filename, "w")
            print "Opening file \"%s\" in write." % output_filename
        except:
            assert False, "Error: could not write file \"%s\"." % output_filename
    else:
        print "Warning: no output file given as argument."
        file_out = None

    return file_in, file_out

def process_test(test_id):
    result = "Case #%d: " % test_id

    C, F, X = map(Decimal, file_in.readline().split(" "))
    #print C, F, X

    current_time_to_buy_farms = 0
    current_rate = Decimal(2)
    current_time_to_win = X / current_rate

    try_again = True
    stop = False
    #iteration = 0
    while (try_again and not stop):
        new_time_to_buy_farms = current_time_to_buy_farms + C / current_rate
        new_rate = current_rate + F
        new_time_to_win = new_time_to_buy_farms + X / new_rate

        #print time_to_buy_farm
        #print new_rate
        #print current_time_to_win, new_time_to_win

        #if iteration > :
        #    stop = True

        if new_time_to_win < current_time_to_win:
            try_again = True
            current_time_to_buy_farms = new_time_to_buy_farms
            current_rate = new_rate
            current_time_to_win = new_time_to_win
        else:
            try_again = False
            result += "%.7f" % current_time_to_win

        #iteration += 1



    return result

if __name__ == "__main__":
    start_time = time.time()

    print getcontext()

    # Open input and output files
    file_in, file_out = open_io_files()

    # Extract the number of tests
    T = int(file_in.readline())

    # Process every test and write to file
    for test_id in range(1, T+1):
        result = process_test(test_id)
        if file_out:
            file_out.write(result + "\n")
        else:
            print result

    time = time.time() - start_time
    print "%s executed in %g seconds." % (sys.argv[0], time)
