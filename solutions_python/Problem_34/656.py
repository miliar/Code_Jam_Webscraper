import re
filename = 'A-large.in.txt'

def build_regex(pattern):
    regex = r''
    is_paren = False
    for char in pattern:
        if char == '(':
            is_paren = True
            in_paren ='['
            continue
        if char == ')':
            is_paren = False
            regex += in_paren.rstrip('|') + ']+'
            in_paren = ''
            continue
        if is_paren:
            in_paren += char + '|'
        else:
            regex += '[' + char + ']+'
    regex = regex.rstrip('|')
    return re.compile(regex)


def verify(words, tests):
    result_file = file('result.txt', 'w')
    for i, test in enumerate(tests):
        result = [ w for w in words if test.match(w) ]
        line = 'Case #%d: %d' % (i+1, len(result))
        result_file.write(line + '\n')
    result_file.close()

def main():
    file_obj = file(filename)
    l, d, n = [int(n) for n in file_obj.readline().split()]
    words = []
    while d > 0:
        words.append(file_obj.readline().strip('\n'))
        d -= 1
    
    tests = []
    for line in file_obj:
        tests.append( build_regex(line.strip('\n')) )
    
    file_obj.close()
    
    verify(words, tests)
    

if __name__ == '__main__':
    main()