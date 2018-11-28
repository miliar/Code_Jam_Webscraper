FILENAME = "C-small-attempt0"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME

def scramble(string, start):    
    return string[start:] + string[:start]
    
def scrambles(string):
    output = list()
    
    for i in range(len(string)):
        output.append(scramble(string, i))
        
    return output

def is_recycled(left, right):
    left = str(left)
    right = str(right)
    return left in scrambles(right)

def solve(lines):
    output = 0
    
    start, end = [int(n) for n in lines[0].split(" ")]
    
    for left in range(start, end+1):
        for right in range(left+1, end+1):
            if is_recycled(left, right):
                output += 1
        
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
