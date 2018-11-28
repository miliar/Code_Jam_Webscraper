mapping = {
        'a' : 'y',
        'b' : 'h',
        'c' : 'e',
        'd' : 's',
        'e' : 'o',
        'f' : 'c',
        'g' : 'v',
        'h' : 'x',
        'i' : 'd', 
        'j' : 'u',
        'k' : 'i',
        'l' : 'g',
        'm' : 'l',
        'n' : 'b',
        'o' : 'k',
        'p' : 'r',
        'q' : 'z',
        'r' : 't',
        's' : 'n',
        't' : 'w',
        'u' : 'j',
        'v' : 'p',
        'w' : 'f',
        'x' : 'm',
        'y' : 'a',
        'z' : 'q',
        ' ' : ' '
        }

def translate(line):
    new_line = ''
    for c in line:
        new_line += mapping[c]
        
    return new_line 


if __name__ == "__main__":
    import fileinput 
    for line in fileinput.input():
        if fileinput.isfirstline():
            T = int(line.strip())
        else:
            print "Case #%d: %s" % (fileinput.filelineno()-1, translate(line.strip()))

