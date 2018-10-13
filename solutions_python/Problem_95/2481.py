import string

if __name__ == "__main__":
    i = open("googlereese.txt", "r")
    o = open("english.txt", "r")
    
    # number of cases
    noc = int(i.readline().strip())
    
    # initialize mapping
    mapping = {' ': ' ', 'a': 'y', 'o': 'e', 'z': 'q'}
    
    for x in range(1, noc + 1):
        # read line from the input
        input_line = i.readline().strip()
        # read line from the output
        output_line = o.readline().strip()
        # add letters to the mapping
        for x in range(0, len(input_line)):
            mapping[output_line[x]] = input_line[x]
    
    not_in_googlereese = ''
    not_in_english = ''
    
    letters = string.ascii_lowercase
    
    for x in letters:
        if x not in mapping.values(): not_in_googlereese = x
        if x not in mapping.keys(): not_in_english = x
        if not_in_googlereese != '' and not_in_english != '': break
    
    mapping[not_in_english] = not_in_googlereese
    
    i.close()
    o.close()
    
    mapping_googlereese = ''
    mapping_english = ''
    
    for x, y in mapping.items():
        mapping_googlereese = mapping_googlereese + y
        mapping_english = mapping_english + x
    
    translation_table = "".maketrans(mapping_googlereese, mapping_english)
    
    # got mapping, now to translation
    
    i = open("small.txt", "r")
    o = open("small_output.txt", "w")
    
    # number of cases
    noc = int(i.readline().strip())
    
    for x in range(1, noc + 1):
        # read line from the input
        input_line = i.readline().strip()
        # translate to english
        output_line = input_line.translate(translation_table)
        # add result to output
        o.write("Case #" + str(x) + ": " + output_line + "\n")
    
    i.close()
    o.close()
