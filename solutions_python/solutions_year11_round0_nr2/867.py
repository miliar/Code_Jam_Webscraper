import sys

def parse_case(line):
    fields = line.split()

    generator_dict = {}
    destructor_dict = {}

    num_generators = int(fields[0])
    i = 1
    while i <= num_generators:
        gen_elems = fields[i]
        generator_dict[(gen_elems[0], gen_elems[1])] = gen_elems[2]
        generator_dict[(gen_elems[1], gen_elems[0])] = gen_elems[2]
        i += 1

    num_destructors = int(fields[i])
    i += 1
    j = 0
    while j < num_destructors:
        dest_elems = fields[i+j]
        destructor_dict.setdefault(dest_elems[0], set()).add(dest_elems[1])
        destructor_dict.setdefault(dest_elems[1], set()).add(dest_elems[0])
        j += 1

    elem_list = [c for c in fields[i+j+1]]

    return generator_dict, destructor_dict, elem_list

def solve_case(g_dict, d_dict, e_list):
    out_list = []
    for e in e_list:
        outlist_reset = 0
        if out_list and (e, out_list[-1]) in generator_dict:
            out_list[-1] = generator_dict[(e, out_list[-1])]
            e = ''

        if e:
            dest_set = destructor_dict.get(e, set())
            for i in out_list:
                if i in dest_set:
                    out_list = []
                    outlist_reset = 1
                    break

            if not outlist_reset:
                out_list.append(e)
        elif out_list:
            ''' meaning e was reset followin a combination'''
            el_to_chk = out_list[-1]
            out_list = out_list[:-1]
            dest_set = destructor_dict.get(el_to_chk, set())
            for i in out_list:
                if i in dest_set:
                    out_list = []
                    outlist_reset = 1
                    break

            if not outlist_reset:
                out_list.append(el_to_chk)

    return out_list
        


if __name__ == '__main__':
    indata = open(sys.argv[1], 'r').read().split('\n')
    ofd = open(sys.argv[2], 'w')
    num_cases = int(indata[0])
    case_id = 1
    while case_id <=  num_cases:
        line = indata[case_id]
        generator_dict, destructor_dict, elem_list = parse_case(line)
        out_list =  solve_case(generator_dict, destructor_dict, elem_list)
        ofd.write('Case #%s: [%s]\n' % (case_id, ', '.join(out_list)))
        case_id += 1
    ofd.close()
