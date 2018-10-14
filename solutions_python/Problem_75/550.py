
def solver(combines, opposed, elems):
    combine_dict = {}
    opposed_dict = {}
    for c in combines:
        if c[0] not in combine_dict:
            combine_dict[c[0]] = {}
        combine_dict[c[0]][c[1]] = c[2]
        if c[1] not in combine_dict:
            combine_dict[c[1]] = {}
        combine_dict[c[1]][c[0]] = c[2]

    for c in opposed:
        opposed_dict[c[0]] = c[1]
        opposed_dict[c[1]] = c[0]

    elem_stack = []
    for elem in elems:
        print 'elem ', elem
        print 'elem_stack ', elem_stack
        finished = 0
        if len(elem_stack) > 0 and elem_stack[-1] in combine_dict.get(elem, {}):
            new_elem = combine_dict[elem][elem_stack[-1]]
            elem_stack.pop()
            elem_stack.append(new_elem)
            finished = 1
        elif elem in opposed_dict:
            for opp in opposed_dict[elem]:
                try:
                    elem_stack.index(opp)
                    elem_stack = []
                    finished = 1
                except:
                    pass
        if not finished:
            elem_stack.append(elem)
    return elem_stack




def ssi(s):
    """
    space separated integers
    """
    return map(int, s.strip('\n').split())

def main():
    # open input file
    input_file = open('infile.txt')
    cases = int(input_file.readline())
    output = []
    # loop through cases passing input to solver
    for c in range(cases):
        l = input_file.readline().strip('\n').split()
        num_combines = int(l.pop(0))
        combines = l[:num_combines]
        l = l[num_combines:]
        num_opposed = int(l.pop(0))
        opposed = l[:num_opposed]
        l = l[num_opposed:]
        num_elems = int(l.pop(0))
        elems = list(l.pop())
        print 'combines' , combines
        print 'opposed', opposed
        print 'elems', elems
        answer = solver(combines, opposed, elems)
        output.append('Case #%d: %s\n' % (c+1, str(answer).replace("'", "")))
    input_file.close()
    # open output file
    output_file = open('outfile.txt', 'w')
    # write ouput to file
    output_file.writelines(output)
    # close out file
    output_file.close()
    print 'Done!'



if __name__=='__main__':
    main()
