
def is_destroy(char,result,destroy_list):
    for s in result:
        if char in destroy_list and s in destroy_list[char]:
            return True
    return False

def MAGICKA():
    testcases = int(raw_input())
    for case in xrange(0,testcases):
        input = raw_input().split()
        combine_count = int(input[0])
        destroy_count = int(input[1+combine_count])
        combine_elements = []
        destroy_elements = []
        for i in xrange(1,1+combine_count):
            combine_elements.append(input[i])
        for i in xrange(combine_count+2,combine_count+2+destroy_count):
            destroy_elements.append(input[i])
        sequence = input[combine_count+2+destroy_count+1]
        combine_matrix = {}
        destroy_list = {}
        for elem in combine_elements:
            combine_matrix[(elem[0],elem[1])] = elem[2]
            combine_matrix[(elem[1],elem[0])] = elem[2]
        for elem in destroy_elements:
            if not elem[0] in destroy_list:
                destroy_list[elem[0]] = [elem[1]]
            else:
                destroy_list[elem[0]].append(elem[1])
            if not elem[1] in destroy_list:
                destroy_list[elem[1]] = [elem[0]]
            else:
                destroy_list[elem[1]].append(elem[0])
        result = []
        for i in xrange(0,len(sequence)):
            char = sequence[i]
            if not result:
                result.append(char)
                continue
            pair = (char,result[len(result)-1])
            if pair in combine_matrix:
                result[len(result)-1] = combine_matrix[pair]
            elif is_destroy(char, result, destroy_list):
                result = []
            else:
                result.append(char)
        builder = 'Case #' + str(case+1) + ': ['
        for r in result:
            builder = builder + r + ', '
        if builder[-1] != '[':
            builder = builder[:-2] + ']'
        else:
            builder = builder + ']'
        print builder
MAGICKA()


        
