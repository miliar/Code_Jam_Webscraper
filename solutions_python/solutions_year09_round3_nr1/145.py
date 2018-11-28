def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    out_lines = []
    
    T = int(lines.pop(0))
    
    def to_base_10(num, base):
        ret = 0
        for i, digit in enumerate(num):
            ret += lang[digit] * base**(len(num) - i - 1)
        return ret
    
    for case in xrange(T):
        lang = {}
        V = 0L
        
        alien_num = lines.pop(0).replace('\n', '')
        
        next_num = 2
        base = 2
        for char in alien_num:
            if char not in lang:
                if len(lang) == 0:
                    lang[char] = 1
                elif len(lang) == 1:
                    lang[char] = 0
                else:
                    lang[char] = next_num
                    next_num += 1
                    base += 1
        
        V = to_base_10(alien_num, base)
        
        line = 'Case #%i: %i\n' %((case + 1), V)
        print line
        out_lines.append(line)
    
    f = open('A.out', 'w')
    f.writelines(out_lines)
    f.close()
    

if __name__ == '__main__':
    main('A-large.in')
#    main('testa')