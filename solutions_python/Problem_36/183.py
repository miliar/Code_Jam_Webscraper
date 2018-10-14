def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    outlines = []
    
    N = int(lines.pop(0))
    
    for case in xrange(N):
        num = 0
        input = lines.pop(0)
        
        full_string = 'welcome to code jam'
        num_substr = {}
        
        for i in xrange(len(full_string)):
            num_substr[full_string[:i + 1]] = 0
        
        active_strings = []
        
        for char in input:
            if char == 'w':
                num_substr[char] = (num_substr[char] + 1) % 10000
                if char not in active_strings:
                    active_strings.append(char)
            else:
                for s in active_strings:
                    concat = s + char
                    if concat in num_substr:
                        num_substr[concat] = (num_substr[concat] + num_substr[s]) % 10000
                        if concat not in active_strings:
                            active_strings.append(concat)
        
        line = 'Case #%i: %04d\n' % ((case + 1), num_substr[full_string])
        print line
        outlines.append(line)
    
    f = open('C.out', 'w')
    f.writelines(outlines)
    f.close()

if __name__ == "__main__":
    main('C-large.in')