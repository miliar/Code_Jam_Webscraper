import sys

def do_test_case(ofile, curr_test_case, first_ans, first_rows, second_ans, second_rows):

    first_set = set(first_rows[first_ans - 1])
    second_set = set(second_rows[second_ans - 1])
    both = first_set.intersection(second_set)

    if len(both) == 1:
        result = str(both.pop())
    elif len(both) == 0:
        result = "Volunteer cheated!"
    else: # len(both) > 1
        result = "Bad magician!" 
    
    print 'Case #%d: %s' % (curr_test_case, result)
    ofile.write('Case #%d: %s' % (curr_test_case, result) + "\n")

def main():
    if len(sys.argv) != 3:
        print "Usage: ProblemA.py <input> <output>"
        exit()

    with open(sys.argv[1], 'r') as ifile:
        with open(sys.argv[2], 'w') as ofile:
            ilines = ifile.readlines()
            ncases = int(ilines[0])
            ilines_idx = 1

            for curr_test_case in range(1, ncases + 1):
                first_ans = int(ilines[ilines_idx]); ilines_idx += 1;
                first_rows = []
                for row in range(0,4):
                    first_rows.append(map(lambda a: int(a), ilines[ilines_idx].split()))
                    ilines_idx += 1
                    
                second_ans = int(ilines[ilines_idx]); ilines_idx += 1;
                second_rows = []
                for row in range(0,4):
                    second_rows.append(map(lambda a: int(a), ilines[ilines_idx].split()))
                    ilines_idx += 1

                do_test_case(ofile, curr_test_case, first_ans, first_rows, second_ans, second_rows)
                
                
                

if __name__ == "__main__":
    main()
