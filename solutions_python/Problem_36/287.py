import sys

class Case(object):
    def __init__(self, case_no):
        self.case_no = case_no
        self.text = ''
        
    def output(self):
        num_found = str(self.num_found)
        if len(num_found) < 4:
            num_found = '0'*(4-len(num_found)) + num_found
        return 'Case #%s: %s' % (self.case_no, num_found[-4:])

def get_line(f):
    line = f.readline()
    if line[:-1] == '\n':
        line = line[:-1]
    return line
    
def process_input(file_name):
    all_cases = []
    f = file(file_name)
    line = get_line(f)
    num_cases = int(line)
    for x in range(num_cases):
        case = Case(x + 1)
        case.text = get_line(f)
        all_cases.append(case)
    return all_cases

cache = {}
def calc_num_found(search_for, text):
    if (search_for, text) in cache:
        return cache[(search_for, text)]
    if len(search_for) > text:
        return 0
    if len(search_for) == len(text):
        if search_for == text:
            return 1
        else:
            return 0
    
    num_found = 0
    for ix, letter in enumerate(text):
        if letter == search_for[0]:
            if len(search_for) == 1:
                num_found += 1
                continue
            num_found += calc_num_found(search_for[1:], text[ix+1:])
    cache[(search_for, text)] = num_found
    return num_found
            

if __name__ == '__main__':
    input_file_name = sys.argv[-1]
    output_file = input_file_name.split('.')[0] + '.out'
    all_cases = process_input(input_file_name)
    for case in all_cases:
        print 'process case', case.case_no
        case.num_found = calc_num_found('welcome to code jam', case.text)
    f = file(output_file, 'wb')
    out =''
    for case in all_cases:
        out += case.output() + '\n'
    
    f.write(out)
    f.close()
    
    