
import re

def generate_regex(s):
    p = False
    r = ''
    
    for c in s:
        if '(' == c:
            p = True
        elif ')' == c:
            p = False
        
        r += c
        
        if p:
            r += '|'
    
    r = r.replace('(|', '[')
    r = r.replace('|)', ']')
    
    return r

def main():
    FILENAME = 'A-large'
    
    output = open(FILENAME + '.out', 'w')
    lines = open(FILENAME + '.in', 'r').readlines()
    
    parts = lines[0].split()
    count = int(parts[0])
    dictionary = lines[1:1 + int(parts[1])]
    lines = lines[1 + int(parts[1]):]
    
    for i in range(len(lines)):
        line = lines[i].strip()
        regexp_text = generate_regex(line)
        regexp = re.compile(regexp_text)
        matched = 0
        
        for e in dictionary:
            if e and re.match(regexp, e):
                matched += 1
        
        output.write("Case #%d: %s\n" % (i + 1, matched))
    
    output.close()

if __name__ == '__main__':
    main()