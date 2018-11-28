import string

aaafrom = "abcdefghijklmnopqrstuvwxyz"
mapping = "ynficwlbkuomxsevzpdrjgthaq"

filename = "text.in"

def read_input():
    trantab = string.maketrans(mapping, string.ascii_lowercase)
    f = open(filename)
    lines = f.readlines()
    test_case = int(lines[0])
    case_num = 0
    for line in lines[1:]:
        result = line.translate(trantab)
        case_num = case_num + 1
        output_result(case_num, result)

def output_result(case_num, result):
    print "Case #%d: %s" % (case_num, result)
    


if __name__=='__main__':
    
    read_input()
