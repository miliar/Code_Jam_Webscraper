from pprint import pprint
import pdb

def tokenize(pattern):
    l = []
    temp = []

    flag = 0
    for i in range(0, len(pattern)):
        if pattern[i] == '(':
            flag = 1
            continue
        if pattern[i] == ')':
            l.append(temp)
            temp = []
            flag = 0
            continue
        if(flag):
            temp.append(pattern[i])
        else :
            l.append(list(pattern[i]))

    return l

def is_text_in_pattern(text, pattern):
    for i in range(0, len(text)):
        if(text[i] not in pattern[i]):
            return False

    return True

def dict_match_pattern(alien_dict, pattern):
    count = 0
    for i in range(0, len(alien_dict)):
        if is_text_in_pattern(alien_dict[i], pattern):
            count = count + 1

    return count

        
def main():
    with open(r'F:\Python_tut\CodeJam2009\A\A-large.in', 'r') as f:
        input_size = f.readline()
        (l, d, n) = input_size.split()

        alien_dict = []
        for i in range(0, int(d)):
            temp = f.readline(int(l))
            f.readline()
            alien_dict.append(temp)

        lines = f.readlines()
        case_num = 0
        for line in lines:
            case_num = case_num + 1
            pattern = tokenize(line[0:-1])
            print('Case #%d: %d' %
                  (case_num, dict_match_pattern(alien_dict, pattern)))
                   

if __name__=='__main__':
##    pdb.set_trace()
    main()
