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

    # get self
    me, nb_other = map(int, file_in.readline().split(" "))
    other_l = map(int, file_in.readline().split(" "))
    other_l.sort()
    new_other_l = other_l[:]
    #print me, nb_other, other_l

    exit = False
    cnt = 0
    ref_size = len(other_l)
    while other_l and not exit:
        #print "me", me
        if other_l[0] < me:
            #print "smaller, absorb", other_l[0]
            me += other_l[0]
        else:
            #print "greater or equal", other_l[0]
            list_size = len(other_l)
            me_tmp = me
            cnt_tmp = cnt
            found = False
            for i in range(list_size):
                me_tmp_old = me_tmp
                me_tmp += (me_tmp - 1)
                cnt_tmp += 1
                if me_tmp > other_l[0]:
                    #print "add mobe %d and absorb %d" % (me_tmp_old - 1, other_l[0])
                    me = me_tmp + other_l[0]
                    cnt = cnt_tmp
                    found = True
                    break
                else:
                    #print "add again me_tmp", me_tmp_old - 1
                    pass
            if not found:
                cnt += 1
                #print "delete mobe", other_l[0]
        del other_l[0]

        if cnt > ref_size:
            cnt = ref_size

#        for index, item in enumerate(other_l):
#            print index, item, me
#            if item < me:
#                print "smaller, restart"
#                me += item
#                del other_l[index]
#                break
#            else:
#                print "greater or equal"
#                cnt += 1
#                if (me + (me - 1)) > item:
#                    me += (me - 1)
#                    break
#                else:
#                    del other_l[index]
#                    break
#                exit = True

#    print new_other_l

    result += " %d" % cnt
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
