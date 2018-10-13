#/usr/bin/python
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    infile = sys.argv[1]
    print infile 
    with open(infile) as f:
        num_tests = int(f.readline())
        print "number of tests: {0}".format(num_tests)
        case_number = 1
        solutions = {}
        for line in f:
            print "Solving case #{0}".format(case_number)
            splitline = line.split()
            combining_elements = {}
            num_comb = int(splitline[0])
            for comb_elems in splitline[1: num_comb+1]:
                combining_elements[comb_elems[0]] = {comb_elems[1]: comb_elems[2]}
                combining_elements[comb_elems[1]] = {comb_elems[0]: comb_elems[2]}
            oposing_elements = {}
            splitline = splitline[num_comb+1:]
            num_opo = int(splitline[0])
            for op_elems in splitline[1: num_opo+1]:
                oposing_elements[op_elems[0]] = op_elems[1]
                oposing_elements[op_elems[1]] = op_elems[0]
            splitline = splitline[num_opo+1:]
            element_list = []
            for element in splitline[1]:
                element_list.append(element)
                #print element
                if len(element_list) > 1 and element in combining_elements and element_list[-2] == combining_elements[element].keys()[0]:
                    second_element = element_list[-2]
                    element_list.pop()
                    element_list.pop()
                    element_list.append(combining_elements[element][second_element])
                    continue
                if element in oposing_elements and oposing_elements[element] in element_list:
                    element_list = []
            solutions[case_number] = element_list[:]
            case_number += 1
    outfile = sys.argv[2]
    with open(outfile, 'w') as of:
        for solution in solutions:
            of.write('Case #{0}: [{1}]\n'.format(solution, ', '.join(solutions[solution]))) 
