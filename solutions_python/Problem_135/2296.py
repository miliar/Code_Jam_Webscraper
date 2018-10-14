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
    result = "Case #%d:" % test_id

    answer_l = []
    row_l = [[], []]
    for part in range(2):
        answer_l.append(int(file_in.readline().rstrip("\n").split(" ")[0]))
        for row in range(4):
            row_l[part].append(map(int, file_in.readline().rstrip("\n").split(" ")))
        print answer_l
        print row_l

    select1 = row_l[0][answer_l[0]-1]
    select2 = row_l[1][answer_l[1]-1]

    print select1
    print select2

    cards_possible = set(select1) & set(select2)
    print cards_possible

    nb_cards_possible = len(cards_possible)

    if nb_cards_possible == 0:
        result += " Volunteer cheated!"
    elif nb_cards_possible == 1:
        result += " %d" % (list(cards_possible)[0])
    else:
        result += " Bad magician!"

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
            file_out.write(result + "\n")
        else:
            print result

    time = time.time() - start_time
    print "%s executed in %g seconds." % (sys.argv[0], time)
