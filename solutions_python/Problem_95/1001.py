FILENAME = "A-small-attempt0"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME

mapping = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q',
    ' ': ' ',
}

def solve(lines):
    output = ""
    for character in lines[0]:
        output += mapping[character]
        
    return output

if __name__ == '__main__':
    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "w")
    
    cases = int(input_file.readline())
    for case in range(1, cases+1): # Count case from 1, 2, ..., n
        input_lines = list()
        for i in range(LINE_PER_CASE):
            input_lines.append(input_file.readline()[:-1]) # Remove newline
        output_file.write("Case #%d: %s\n" % (
            case,
            solve(input_lines),
        ))
    
    input_file.close()
    output_file.close()
