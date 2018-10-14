import numpy as np

def read_file():
    '''
    Reads the input file
    '''
    n_data = int(raw_input())  # read a line with a single integer
    data = {}
    flip_sizes = []
    for i in range(n_data):
        line = raw_input()
        current_line = []
        flip_size = -1
        test_line = ""
        for d, di in zip(line, range(len(line))):
            if flip_size == -1:
                if d == '-':
                    current_line.append(False)
                    test_line += "-"
                elif d == " ":
                    flip_size = 1
                else:
                    current_line.append(True)
                    test_line += "+"
            else:
                flip_sizes.append(int(line[di:]))
                test_line += " {}".format(int(line[di:]))
                break

        #print test_line
        data[i] = np.array(current_line)

    return data, flip_sizes

def write_file(data):
    '''
    write the output file for the passed pizza
    '''
    # number of slices
    for i, d in zip(range(len(data)), data):
        if d == -1:
            line = "Case #{}: INSOMNIA".format(i+1)
        else:
            line = "Case #{}: {}".format(i+1, d)
        print(line)


def solve_problem(data, flip_sizes):
    for i, ds in zip(range(len(flip_sizes)), flip_sizes):
        current = data[i]
        flip_i = 0
        current_col = 0
        fail = False
        if not np.all(current):  # all are good
            while True:
                if current_col + ds > len(current):
                    if not np.all(current[current_col:current_col + ds]):
                        # end is not OK
                        fail = True
                    break
                else:
                    if not current[current_col]:
                        flip_i += 1
                        for j in range(ds):
                            if current[current_col+j]:
                                current[current_col+j] = False
                            else:
                                current[current_col+j] = True

                    current_col += 1
                    if current_col >= len(current):
                        current_col -= 1
                        break
        if fail:
            line = "Case #{}: IMPOSSIBLE".format(i+1)
        else:
            line = "Case #{}: {}".format(i+1, flip_i)
        print(line)

if __name__ == '__main__':
    #filename = sys.argv[1]
    #print filename
    # read
    data, flip_sizes = read_file()
    #print len(data.keys())
    #print len(flip_sizes)

    # solve
    #print "Solving"
    solve_problem(data, flip_sizes)

    # write
    #outfile = filename.split('.')[0]
    #outfile += ".out"
    #print outfile
    #write_file(result)
