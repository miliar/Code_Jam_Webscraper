def cjwrap(answerer, input_filename):
    fin = file(input_filename, 'r')
    fout = file('output.txt', 'w')
    inputs = int(fin.readline())
    for i in xrange(inputs):
        output = answerer(fin)
        fout.write("Case #%s: %s\n" % (i+1, str(output)))
    fout.close()

def answer(f):
    return process_line(f.readline())

def process_line(linestr):
    line = linestr.split(" ")    
    ncombs = int(line[0])
    combinations = {}
    for i in xrange(1, ncombs + 1):
        left = sort_string(line[i][:2])
        right = line[i][-1]
        combinations[left] = right
    
    nopposed = int(line[ncombs + 1])
    opposed = []
    for i in xrange(ncombs + 2, ncombs + nopposed + 2):
        opposed.append(sort_string(line[i]))
        
    str = line[-1]
    if str[-1] == '\n':
        str = str[:-1]
    # return " ".join(line) + "\t" +
    return process(str, combinations, opposed)
    # print "combinations: ", combinations
    # print "opposed: ", opposed
    # print "str:", str

def sort_string(str):
    l = list(str)
    l.sort()
    return "".join(l)
    
def process(str, combinations, opposed):
    processed = ""
    print "**** handling: ", str, combinations, opposed
    for s in str:
        processed += s
        print "step1 (extending str):", processed
        snapshot = sort_string(processed[-2:])
        if combinations.has_key(snapshot):
            processed = processed[:-2] + combinations[snapshot]
        print "step2 (combinations): ", processed
        for pair in opposed:
            if (pair[0] in processed) and (pair[1] in processed):
                processed = ""  
        print "step3 (oppositions): ", processed
    return "[" + ", ".join(list(processed)) + "]"
  
cjwrap(answer, 'input.txt')