vocab = {' ': ' ',
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
 'z' : 'q'}

def solve(input):
    input = input.strip()
    output = []
    for i, ch in enumerate(input):
        output.append(vocab[ch])
        
    return "".join(output)

def main():
    # Code for Reading and writing.
    # Small Files.
    in_file_name = "A-small-attempt0.in"
    out_file_name = "A-small-attempt0.out"
    
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')
    
    reader.readline()
    for case_no, input in enumerate(reader):
        result = solve(input)
        writer.write("Case #" + str(case_no+1)+ ": " + str(result) + "\n")   
    writer.close()
    
#########################################################
if __name__== "__main__":
    main()