import sys
VERBOSE =  0
def resolve(combined, opposed, elements_str):
    result = []
    for elem in elements_str:
        result.append(elem)
        #more element
        if len(result) > 1:
            #first try combination
            prev_elem = result[-2]
            key = prev_elem + elem
            if key in combined.keys():
                if VERBOSE:
                    print 'found combined "%s"' %key
                result = result[:-2]
                result.append(combined.get(key))
            else:
                opposed_elems = opposed.get(elem, [])
                for o_elem in opposed_elems:
                    if o_elem in result:
                        if VERBOSE:
                            print 'found opposed "%s%s"' %(o_elem, elem)
                        result = []
                        continue
    return result
    
def main():
    file = open(sys.argv[1])
    length = file.readline()
    case_num = 1
    for line in file.readlines():
        case_list = line.split(' ')
        num_combine = int(case_list[0])
        if num_combine == 0:
            combined = {}
        else:
            _combined = [(item[:2], item[2]) for item in case_list[1: num_combine+1]]
            combined = dict(_combined)
            _combined = [(item[-2::-1], item[2]) for item in case_list[1: num_combine+1]]
            combined_2 = dict(_combined)
            combined.update(combined_2)
        num_opposed = int(case_list[num_combine+1])
        if num_opposed == 0:
            opposed = {}
        else:
            opposed = {}
            _opposed = case_list[num_combine+2: -2]
            for item in _opposed:
                x = item[0]
                y = item[1]
                opposed.setdefault(x,[]).append(y)
                opposed.setdefault(y,[]).append(x)
        elements_str = case_list[-1].strip()
        if VERBOSE:
            print '-'*20
            print 'C: ', num_combine
            print 'O: ', num_opposed
            print 'N: ', case_list[-2]
            print 'combined: %s' %combined
            print 'opposed: %s' %opposed
            print 'elements_str: %s' %elements_str
        result = resolve(combined, opposed, elements_str)
        output = 'Case #%d: %s' %(case_num, result) 
        print output.replace("'","")
        case_num += 1

if __name__ == '__main__':
    main()
