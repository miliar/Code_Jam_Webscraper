import sys

def init_dict(dictionary, input, output):
    for i in range(0, len(input)):
        dictionary[input[i]] = output[i]

def map_string(instr, dict):
    res = ''
    for i in range(0, len(instr)):
        res += dict[instr[i]]
    return res

def main():
    # init dict with predefined pairs
    dictionary = {}
    init_dict(dictionary, "aoz", "yeq") # 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q
    init_dict(dictionary, "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
    init_dict(dictionary, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
    init_dict(dictionary, "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
    init_dict(dictionary, "q", "z") # this is the one missing in examples, I hope noone expect uber code to find it :)
    
    cases = open(sys.argv[1], 'r')
    T = int(cases.readline())
    for i in range(0, T):
        line = cases.readline().strip()
        print "Case #%d: %s" % (i+1, map_string(line, dictionary))
    

main()