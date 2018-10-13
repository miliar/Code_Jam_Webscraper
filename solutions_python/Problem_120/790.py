import sys
import time

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
    r, t = map(int, file_in.readline().rstrip("\n").split(" "))

    remaining_paint = t
    i = 0
    nb_circle = 0
    while remaining_paint > 0:
        if i == 0:
            prev_r = r + 1
            cur_area = prev_r ** 2 - r ** 2
        else:
            #cur_area = (prev_r + 2) ** 2 - (prev_r + 1) ** 2
            cur_area = 3 + 2 * prev_r
            prev_r = prev_r + 2

        #print cur_area
        remaining_paint -= cur_area
        i+=1
        if remaining_paint >= 0:
            nb_circle += 1

    result = "Case #%d: %d\n" % (test_id, nb_circle)

    return result

if __name__ == "__main__":
    start_time = time.time()

    # Open input and output files
    file_in, file_out = open_io_files()

    # Extract the number of tests
    T = int(file_in.readline())

    # Process every test and write to file
    for test_id in range(1, T+1):
        result = process_test(test_id)
        if file_out:
            file_out.write(result)
        else:
            print result

    time = time.time() - start_time
    print "%s executed in %g seconds." % (sys.argv[0], time)
