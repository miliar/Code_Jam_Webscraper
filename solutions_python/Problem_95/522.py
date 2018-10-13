
def get_charmap():
    char_map = {}

    sample_inputs = [
        "y",
        "e",
        "q",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    ]

    sample_outputs = [
        "a",
        "o",
        "z",
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
    ]


    for i in range(len(sample_inputs)):
        input = sample_inputs[i];
        output = sample_outputs[i]
        
        for c in range(len(input)):
            if input[c] == ' ':
                continue
            char_map[input[c]] = output[c]


    input_chars = []
    output_chars = []
    for key, val in char_map.items():
        input_chars.append(key)
        output_chars.append(val)
        
    for input in "abcdefghijklmnopqrstuvwxyz":
        if input not in input_chars:
            for output in "abcdefghijklmnopqrstuvwxyz":
                if output not in output_chars:
                    char_map[input] = output

    return char_map

def solve_case(input, char_map):
    output = ''
    
    for char in input:
        if char == ' ':
            output += char
            continue
        
        output += char_map[char]
    
    return output

def main():
    char_map = get_charmap()
    input = open('A-small-attempt0.in')
    output = open('output.txt', 'w')
    total_case_num = int(input.readline().strip())
    
    for case_num in range(1, total_case_num + 1):
        case = input.readline().strip()
        result = solve_case(case, char_map)
        output.write("Case #%s: %s\n" % (case_num, result))
    

if __name__ == '__main__':
    main()


