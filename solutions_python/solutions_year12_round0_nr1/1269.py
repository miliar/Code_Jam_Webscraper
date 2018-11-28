import string

inp = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""


outp = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""


def make_map():
    mapping = {}
    mapping["q"] = "z"
    mapping["z"] = "q"    
    mapping["y" ] = "a"
    mapping["e"] = "o"
    for x,y in zip(inp, outp):
        if x in mapping:
            if mapping[x] != y:
                raise Exception("bad mapping %s %s" % (x,y))
        else:
            if x in string.lowercase:
                mapping[x] = y

    targets = set(mapping.values())
    
    for s in string.lowercase:
        if s not in mapping:
            print "missing key", s
        if s not in targets:
            print "mssing value", s

    mapping[" "] = " "
    return mapping

def convert(mapping, s):
    return "".join(mapping[x] for x in s)

def run(inputfile):
    mapping = make_map()
    junk = inputfile.readline()
    case = 1
    for line in inputfile:
        print "Case #%d: %s" % (case, convert(mapping, line.rstrip()))
        case += 1

if __name__ == "__main__":
    import sys
    run(open(sys.argv[1]))
    

            
