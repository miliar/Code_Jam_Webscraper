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

    #C, F, X = map(Decimal, file_in.readline().split(" "))
    #print C, F, X
    in_l = map(str, file_in.readline().split(" "))
    smax = int(in_l[0])
    s_l = map(int, list(in_l[1].rsplit("\n")[0]))
    #print in_l
    #print smax
    #print s_l
    print "test:", test_id

    cur_s = 0
    save_nb = []
    place_left = []
    MAX = 9
    s_to_add_total = 0
    # how many free places
    for idx2, nb2 in enumerate(s_l):
        nb_already_here = nb2 #*save_nb[idx2]
        nb_place_left = MAX - nb_already_here
        place_left.append(nb_place_left)


    for idx, nb in enumerate(s_l):
        print "cur_s",cur_s
        if cur_s >= idx:
            cur_s += nb
        elif nb > 0:
            s_to_add = idx - cur_s
            s_to_add_total += s_to_add
            print "s_to_add", s_to_add
            print "s_to_add_total", s_to_add_total
            done = False
            for idx2, nb2 in enumerate(place_left[idx:]):
                if done:
                    break
                else:
                    while place_left[idx2] > 0 and not done:
                        place_left[idx2] -= 1
                        cur_s += 1
                        s_to_add -= 1
                        if s_to_add == 0:
                            done = True
            # nb people stands up
            cur_s += nb

    result = "{0}{1:d}".format(result, s_to_add_total)

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
